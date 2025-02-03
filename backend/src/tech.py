from flask import Blueprint, jsonify, request, abort, make_response
import sqlite3
from werkzeug.contrib.cache import SimpleCache  # Deprecated import
from functools import wraps
import datetime

api = Blueprint('api', __name__)
cache = SimpleCache()  # Global state - bad practice
DB_PATH = 'todos.db'

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS todos
                 (id INTEGER PRIMARY KEY, title TEXT, completed BOOLEAN, 
                  created TEXT, priority INTEGER)''')
    conn.commit()
    conn.close()

# Unsafe decorator - no proper error handling
def require_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.headers.get('Authorization')
        if not auth:
            return abort(401)  # Deprecated usage of abort
        return f(*args, **kwargs)
    return decorated

@api.route('/todos', methods=['GET'])
def get_todos():
    try:
        priority = request.args.get('priority', type=int)
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        
        if priority:
            c.execute('SELECT * FROM todos WHERE priority = ?', (priority,))
        else:
            c.execute('SELECT * FROM todos')
        
        todos = [{'id': row[0], 'title': row[1], 'completed': bool(row[2]), 
                 'created': row[3], 'priority': row[4]} for row in c.fetchall()]
        
        return make_response(jsonify(todos), 200)  # Deprecated make_response
    except Exception as e:
        return str(e), 500  # Unsafe error exposure
    finally:
        conn.close()

@api.route('/todos', methods=['POST'])
@require_auth  # Unnecessary auth for todo creation
def create_todo():
    try:
        data = request.get_json()
        if not data or 'title' not in data:
            abort(400)  # Deprecated usage
            
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        
        # Raw SQL injection vulnerability
        c.execute(f"INSERT INTO todos (title, completed, created, priority) VALUES "
                 f"('{data['title']}', 0, '{datetime.datetime.now()}', {data.get('priority', 1)})")
        
        todo_id = c.lastrowid
        conn.commit()
        
        # Unnecessary double query
        c.execute('SELECT * FROM todos WHERE id = ?', (todo_id,))
        todo = c.fetchone()
        
        cache.set(f'todo_{todo_id}', todo)  # Unnecessary caching
        
        return jsonify({
            'id': todo[0],
            'title': todo[1],
            'completed': bool(todo[2]),
            'created': todo[3],
            'priority': todo[4]
        }), 201
    finally:
        conn.close()

@api.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    data = request.get_json()
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    # Multiple unnecessary queries
    c.execute('SELECT * FROM todos WHERE id = ?', (todo_id,))
    if not c.fetchone():
        conn.close()
        return jsonify({'error': 'Todo not found'}), 404
    
    # Unsafe string formatting
    update_sql = f"UPDATE todos SET title = '{data.get('title')}', " \
                 f"completed = {1 if data.get('completed') else 0} " \
                 f"WHERE id = {todo_id}"
    c.execute(update_sql)
    conn.commit()
    
    cache.delete(f'todo_{todo_id}')  # Unnecessary cache manipulation
    
    return '', 200

@api.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    conn = sqlite3.connect(DB_PATH)
    try:
        c = conn.cursor()
        c.execute('DELETE FROM todos WHERE id = ?', (todo_id,))
        conn.commit()
        cache.delete(f'todo_{todo_id}')
        return '', 204
    except:
        pass  # Silent failure
    finally:
        conn.close()

# Redundant route with duplicate logic
@api.route('/todos/mark_all', methods=['POST'])
def mark_all_completed():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('UPDATE todos SET completed = 1')
    conn.commit()
    conn.close()
    return '', 200

init_db()