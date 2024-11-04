import React, { useEffect, useState } from 'react';
import { fetchOrderStatuses, updateOrderStatus } from '../services/api';

const OrderList = ({ orders, onStatusChange }) => {
  const [statuses, setStatuses] = useState([]);
  const [selectedStatus, setSelectedStatus] = useState({});
  const [editingOrderId, setEditingOrderId] = useState(null);

  useEffect(() => {
    // Получаем статусы из бэкенда при монтировании компонента
    const loadStatuses = async () => {
      try {
        const response = await fetchOrderStatuses();
        setStatuses(response.data.statuses);
      } catch (error) {
        console.error('Ошибка при загрузке статусов:', error);
      }
    };
    loadStatuses();
  }, []);

  const handleStatusChange = async (orderId) => {
    try {
      await onStatusChange(orderId, selectedStatus[orderId]);
      setEditingOrderId(null); // Закрываем редактирование после сохранения
    } catch (error) {
      console.error('Ошибка при изменении статуса:', error);
    }
  };

  return (
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>Вес</th>
          <th>Откуда</th>
          <th>Куда</th>
          <th>Цена</th>
          <th>История статусов</th>
          <th>Изменить статус</th>
        </tr>
      </thead>
      <tbody>
        {orders.map(order => (
          <tr key={order.id}>
            <td>{order.id}</td>
            <td>{order.weight}</td>
            <td>{order.source_location}</td>
            <td>{order.destination_location}</td>
            <td>{order.total_price}</td>
            <td>
              {order.order_statuses.map((status, index) => (
                <div key={index}>
                  {status.description} — {new Date(status.created_at).toLocaleString()}
                </div>
              ))}
            </td>
            <td>
              {editingOrderId === order.id ? (
                <div>
                  <select
                    value={selectedStatus[order.id] || ''}
                    onChange={(e) => setSelectedStatus({
                      ...selectedStatus,
                      [order.id]: e.target.value
                    })}
                  >
                    <option value="">Выберите статус</option>
                    {statuses.map(status => (
                      <option key={status.id} value={status.id}>
                        {status.description}
                      </option>
                    ))}
                  </select>
                  <button onClick={() => handleStatusChange(order.id)}>
                    Сохранить
                  </button>
                  <button onClick={() => setEditingOrderId(null)}>
                    Отмена
                  </button>
                </div>
              ) : (
                <button onClick={() => setEditingOrderId(order.id)}>
                  Изменить статус
                </button>
              )}
            </td>
          </tr>
        ))}
      </tbody>
    </table>
  );
};

export default OrderList;
