# README.md for the todo-app project

# Todo App

This project is a simple To-Do application with a Python backend using Flask and a React frontend built with Vite. 

## Project Structure

```
todo-app
├── backend
│   ├── src
│   ├── requirements.txt
│   └── README.md
└── frontend
    ├── src
    ├── index.html
    ├── package.json
    ├── tsconfig.json
    ├── vite.config.ts
    └── README.md
```

## Backend

The backend is built using Flask and provides a RESTful API for managing to-do items. 

### Setup Instructions

1. Navigate to the `backend` directory.
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the application:
   ```
   python src/app.py
   ```

## Frontend

The frontend is built using React and Vite. 

### Setup Instructions

1. Navigate to the `frontend` directory.
2. Install the required dependencies:
   ```
   npm install
   ```
3. Start the development server:
   ```
   npm run dev
   ```

## Usage

- The backend API can be accessed at `http://localhost:5000/api/todos`.
- The frontend application can be accessed at `http://localhost:3000`.

## Contributing

Feel free to submit issues or pull requests for improvements!