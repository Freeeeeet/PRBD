import React, { useState } from 'react';
import { login } from '../services/api';

const LoginForm = ({ onLogin }) => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = async (e) => {
  e.preventDefault();
  try {
    const data = await login(email, password); // Получаем уже data, а не response.data
    localStorage.setItem('token', data.token); // Сохраняем token из data
    onLogin();
  } catch (error) {
    alert('Ошибка входа. Проверьте логин и пароль.');
  }
};

  return (
    <form onSubmit={handleSubmit}>
      <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} placeholder="Email" required />
      <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} placeholder="Password" required />
      <button type="submit">Войти</button>
    </form>
  );
};

export default LoginForm;