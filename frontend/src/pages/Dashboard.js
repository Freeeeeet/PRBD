import React, { useEffect, useState } from 'react';
import { fetchAllOrders } from '../services/api';
import OrderList from '../components/OrderList';

const Dashboard = () => {
  const [orders, setOrders] = useState([]);
  const [offset, setOffset] = useState(0);
  const limit = 10; // количество заказов на странице

  useEffect(() => {
    const loadOrders = async () => {
      const token = localStorage.getItem('token');
      try {
        const response = await fetchAllOrders(token, offset, limit);
        setOrders(response.data);
      } catch (error) {
        console.error('Ошибка при загрузке заказов:', error);
      }
    };
    loadOrders();
  }, [offset]);

  const handleNext = () => setOffset(offset + limit);
  const handlePrev = () => setOffset(Math.max(0, offset - limit));

  return (
    <div className="container">
      <h2>Панель управления</h2>
      <OrderList orders={orders} />
      <div>
        <button onClick={handlePrev} disabled={offset === 0}>Предыдущая страница</button>
        <button onClick={handleNext}>Следующая страница</button>
      </div>
    </div>
  );
};

export default Dashboard;