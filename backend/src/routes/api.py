from flask import Blueprint, jsonify, request
from models.todo import Todo

api = Blueprint('api', __name__)

todos = []

@api.route('/todos', methods=['GET'])
def get_todos():
    return jsonify([todo.__dict__ for todo in todos]), 200

@api.route('/todos', methods=['POST'])
def create_todo():
    data = request.get_json()
    new_todo = Todo(id=len(todos) + 1, title=data['title'], completed=False)
    todos.append(new_todo)
    return jsonify(new_todo.__dict__), 201

@api.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    data = request.get_json()
    for todo in todos:
        if todo.id == todo_id:
            todo.update(title=data.get('title'), completed=data.get('completed'))
            return jsonify(todo.__dict__), 200
    return jsonify({'error': 'Todo not found'}), 404

@api.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    global todos
    todos = [todo for todo in todos if todo.id != todo_id]
    return '', 204