import React, { useState } from 'react';
import { updateOrderStatus } from '../services/api';

const OrderStatusUpdateForm = ({ onStatusUpdated }) => {
  const [orderId, setOrderId] = useState('');
  const [statusId, setStatusId] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const token = localStorage.getItem('token');
      await updateOrderStatus({ order_id: orderId, status_id: statusId }, token);
      alert('Статус заказа обновлен!');
      onStatusUpdated();
    } catch (error) {
      alert('Ошибка обновления статуса заказа');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input type="number" value={orderId} onChange={(e) => setOrderId(e.target.value)} placeholder="ID заказа" required />
      <input type="number" value={statusId} onChange={(e) => setStatusId(e.target.value)} placeholder="ID статуса" required />
      <button type="submit">Обновить статус</button>
    </form>
  );
};

export default OrderStatusUpdateForm;