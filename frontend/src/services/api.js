import axios from 'axios';

const API_BASE = 'https://prometheussiptelepony.space/proekt-db/api';

// Функция для входа
export const login = async (email, password) => {
  try {
    const response = await axios.post(`${API_BASE}/user/login`, { email, password });

    // Сохраняем токен в localStorage, если он есть в ответе
    if (response.data.token) {
      localStorage.setItem('token', response.data.token);
    }

    return response.data;
  } catch (error) {
    console.error('Ошибка при входе:', error);
    throw error;
  }
};

// Функция для получения списка заказов с пагинацией
export const fetchAllOrders = (offset = 0, limit = 10) => {
  const token = localStorage.getItem('token'); // Получаем токен из localStorage
  return axios.get(`${API_BASE}/orders/`, {
    headers: { token }, // Передаем токен в заголовке
    params: { offset, limit }
  });
};

// Функция для создания заказа
export const createOrder = (orderData) => {
  const token = localStorage.getItem('token'); // Получаем токен из localStorage
  return axios.post(`${API_BASE}/orders/create/`, orderData, {
    headers: { token }, // Передаем токен в заголовке
  });
};

// Функция для получения списка заказов
export const fetchOrders = () => {
  const token = localStorage.getItem('token'); // Получаем токен из localStorage
  return axios.get(`${API_BASE}/orders`, {
    headers: { token }, // Передаем токен в заголовке
  });
};

// Функция для обновления статуса заказа
export const updateOrderStatus = (statusData) => {
  const token = localStorage.getItem('token'); // Получаем токен из localStorage
  return axios.post(`${API_BASE}/orders/change_order_status/`, statusData, {
    headers: { token }, // Передаем токен в заголовке
  });
};