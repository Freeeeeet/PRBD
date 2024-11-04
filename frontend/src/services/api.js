import axios from 'axios';

const API_BASE = 'https://prometheussiptelepony.space/proekt-db/api';

//// Функция для входа
//export const login = (email, password) =>
//  axios.post(`${API_BASE}/user/login`, { email, password });

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
export const fetchAllOrders = (token, offset = 0, limit = 10) =>
  axios.get(`${API_BASE}/orders/`, {
    headers: { token: `${token}` },
    params: { offset, limit }
  });

// Функция для создания заказа
export const createOrder = (orderData, token) =>
  axios.post(`${API_BASE}/orders/create/`, orderData, {
    headers: { token: `${token}` },
  });

// Функция для получения списка заказов
export const fetchOrders = (token) =>
  axios.get(`${API_BASE}/orders`, {
    headers: { token: `${token}` },
  });

// Функция для обновления статуса заказа
export const updateOrderStatus = (statusData, token) =>
  axios.post(`${API_BASE}/orders/change_order_status/`, statusData, {
    headers: { token: `${token}` },
  });