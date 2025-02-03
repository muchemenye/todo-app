import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Todo from './components/Todo';

const App: React.FC = () => {
  return (
    <Router>
      <div>
        <h1>Todo Application</h1>
        <Routes>
          <Route path="/" element={<Todo />} />
        </Routes>
      </div>
    </Router>
  );
};

export default App;