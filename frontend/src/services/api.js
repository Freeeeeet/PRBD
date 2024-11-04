import axios from 'axios';

const API_BASE = 'https://prometheussiptelepony.space/proekt-db/api';

// Функция для входа
export const login = (email, password) =>
  axios.post(`${API_BASE}/user/login`, { email, password });

// Функция для получения списка заказов с пагинацией
export const fetchAllOrders = (token, offset = 0, limit = 10) =>
  axios.get(`${API_BASE}/orders/`, {
    headers: { Authorization: `Bearer ${token}` },
    params: { offset, limit }
  });

// Функция для создания заказа
export const createOrder = (orderData, token) =>
  axios.post(`${API_BASE}/orders/create/`, orderData, {
    headers: { Authorization: `Bearer ${token}` },
  });

// Функция для получения списка заказов
export const fetchOrders = (token) =>
  axios.get(`${API_BASE}/orders`, {
    headers: { Authorization: `Bearer ${token}` },
  });

// Функция для обновления статуса заказа
export const updateOrderStatus = (statusData, token) =>
  axios.post(`${API_BASE}/orders/change_order_status/`, statusData, {
    headers: { Authorization: `Bearer ${token}` },
  });