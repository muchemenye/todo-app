import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Todo as TodoType } from '../types';

interface TodoProps {
    id: number;
    title: string;
    completed: boolean;
    onToggle: (id: number) => void;
    onDelete: (id: number) => void;
}

const Todo: React.FC<TodoProps> = ({ id, title, completed, onToggle, onDelete }) => {
    return (
        <div className={`todo-item ${completed ? 'completed' : ''}`}>
            <input
                type="checkbox"
                checked={completed}
                onChange={() => onToggle(id)}
            />
            <span>{title}</span>
            <button onClick={() => onDelete(id)}>Delete</button>
        </div>
    );
};

const TodoList: React.FC = () => {
  const [todos, setTodos] = useState<TodoType[]>([]);
  const [newTodo, setNewTodo] = useState('');
  const API_URL = 'http://localhost:5000/api';

  useEffect(() => {
    fetchTodos();
  }, []);

  const fetchTodos = async () => {
    try {
      const response = await axios.get(`${API_URL}/todos`);
      setTodos(response.data);
    } catch (error) {
      console.error('Error fetching todos:', error);
    }
  };

  const addTodo = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!newTodo.trim()) return;

    try {
      const response = await axios.post(`${API_URL}/todos`, {
        title: newTodo
      });
      setTodos([...todos, response.data]);
      setNewTodo('');
    } catch (error) {
      console.error('Error adding todo:', error);
    }
  };

  const toggleTodo = async (id: number) => {
    try {
      const todo = todos.find(t => t.id === id);
      if (!todo) return;

      await axios.put(`${API_URL}/todos/${id}`, {
        ...todo,
        completed: !todo.completed
      });
      setTodos(todos.map(t => 
        t.id === id ? { ...t, completed: !t.completed } : t
      ));
    } catch (error) {
      console.error('Error toggling todo:', error);
    }
  };

  const deleteTodo = async (id: number) => {
    try {
      await axios.delete(`${API_URL}/todos/${id}`);
      setTodos(todos.filter(t => t.id !== id));
    } catch (error) {
      console.error('Error deleting todo:', error);
    }
  };

  return (
    <div className="todo-container">
      <form onSubmit={addTodo}>
        <input
          type="text"
          value={newTodo}
          onChange={(e) => setNewTodo(e.target.value)}
          placeholder="Add new todo"
        />
        <button type="submit">Add</button>
      </form>

      <div className="todo-list">
        {todos.map((todo) => (
          <Todo
            key={todo.id}
            id={todo.id}
            title={todo.title}
            completed={todo.completed}
            onToggle={toggleTodo}
            onDelete={deleteTodo}
          />
        ))}
      </div>
    </div>
  );
};

export default TodoList;