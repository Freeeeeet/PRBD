import React, { useEffect, useState } from 'react';
import { fetchAllOrders, createOrder } from '../services/api';
import OrderList from '../components/OrderList';

const Dashboard = () => {
  const [orders, setOrders] = useState([]);
  const [offset, setOffset] = useState(0);
  const [weight, setWeight] = useState('');
  const [source, setSource] = useState('');
  const [destination, setDestination] = useState('');
  const [price, setPrice] = useState('');
  const limit = 10; // количество заказов на странице

  useEffect(() => {
    const loadOrders = async () => {
      try {
        const response = await fetchAllOrders(offset, limit); // Убираем передачу token
        setOrders(response.data);
      } catch (error) {
        console.error('Ошибка при загрузке заказов:', error);
      }
    };
    loadOrders();
  }, [offset]);

  const handleNext = () => setOffset(offset + limit);
  const handlePrev = () => setOffset(Math.max(0, offset - limit));

  const handleCreateOrder = async () => {
    const orderData = {
      weight,
      source_location: source,
      destination_location: destination,
      total_price: price
    };
    try {
      await createOrder(orderData);
      alert('Заказ успешно создан');
      setWeight('');
      setSource('');
      setDestination('');
      setPrice('');
      // Обновляем список заказов после создания
      const response = await fetchAllOrders(offset, limit); // Убираем передачу token
      setOrders(response.data);
    } catch (error) {
      console.error('Ошибка при создании заказа:', error);
      alert('Не удалось создать заказ');
    }
  };

  return (
    <div className="container">
      <h2>Панель управления</h2>
      <OrderList orders={orders} />
      <div>
        <button onClick={handlePrev} disabled={offset === 0}>Предыдущая страница</button>
        <button onClick={handleNext}>Следующая страница</button>
      </div>
      <h3>Создать новый заказ</h3>
      <div className="order-form">
        <input
          type="number"
          value={weight}
          onChange={(e) => setWeight(e.target.value)}
          placeholder="Вес"
          required
        />
        <input
          type="text"
          value={source}
          onChange={(e) => setSource(e.target.value)}
          placeholder="Откуда"
          required
        />
        <input
          type="text"
          value={destination}
          onChange={(e) => setDestination(e.target.value)}
          placeholder="Куда"
          required
        />
        <input
          type="number"
          value={price}
          onChange={(e) => setPrice(e.target.value)}
          placeholder="Цена"
          required
        />
        <button onClick={handleCreateOrder}>Создать заказ</button>
      </div>
    </div>
  );
};

export default Dashboard;