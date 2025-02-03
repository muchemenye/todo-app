# README for the Backend

# Todo App Backend

This is the backend for the Todo App, built with Python and Flask. It provides a RESTful API for managing to-do items.

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd todo-app/backend
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   python src/app.py
   ```

## API Usage

### Endpoints

- `GET /api/todos` - Retrieve all to-do items.
- `POST /api/todos` - Create a new to-do item.
- `PUT /api/todos/<id>` - Update an existing to-do item.
- `DELETE /api/todos/<id>` - Delete a to-do item.

## License

This project is licensed under the MIT License.