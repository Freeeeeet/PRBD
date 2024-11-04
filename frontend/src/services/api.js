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
  const token = localStorage.getItem('token');
  return axios.get(`${API_BASE}/orders/`, {
    headers: { token },
    params: { offset, limit }
  });
};

// Функция для создания заказа
export const createOrder = (orderData) => {
  const token = localStorage.getItem('token');
  return axios.post(`${API_BASE}/orders/create/`, orderData, {
    headers: { token },
  });
};

// Функция для получения списка всех доступных статусов заказа
export const fetchOrderStatuses = () => {
  const token = localStorage.getItem('token');
  return axios.get(`${API_BASE}/order_statuses`, {
    headers: { token },
  });
};

// Функция для обновления статуса заказа
export const updateOrderStatus = (orderId, statusId) => {
  const token = localStorage.getItem('token');
  return axios.post(`${API_BASE}/change_order_status/`, { order_id: orderId, status_id: statusId }, {
    headers: { token },
  });
};