import React, { useState } from 'react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import LoginPage from './pages/LoginPage';
import Dashboard from './pages/Dashboard';
import './App.css';

function App() {
  const [isAuthenticated, setIsAuthenticated] = useState(!!localStorage.getItem('token'));

  const handleLogin = () => setIsAuthenticated(true);

  return (
    <BrowserRouter basename="/proekt-db">  {/* Указываем базовый путь для роутинга */}
      <Routes>
        <Route
          path="/"
          element={
            isAuthenticated
              ? <Navigate to="/dashboard" replace />
              : <LoginPage onLogin={handleLogin} />
          }
        />
        <Route
          path="/dashboard"
          element={
            isAuthenticated
              ? <Dashboard />
              : <Navigate to="/" replace />
          }
        />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
