import React, { useState } from 'react';
import { createOrder } from '../services/api';

const OrderForm = ({ onOrderCreated }) => {
  const [weight, setWeight] = useState('');
  const [source, setSource] = useState('');
  const [destination, setDestination] = useState('');
  const [price, setPrice] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const token = localStorage.getItem('token');
      await createOrder({ weight, source_location: source, destination_location: destination, total_price: price }, token);
      alert('Заказ создан успешно!');
      onOrderCreated();
    } catch (error) {
      alert('Ошибка создания заказа');
    }
  };

  return (
    <form onSubmit={handleSubmit} className="order-form">
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
      <button type="submit">Создать заказ</button>
    </form>
  );
};

export default OrderForm;