import React, { useEffect, useState } from 'react';
import { fetchOrderStatuses, updateOrderStatus, updateOrder } from '../services/api';

const OrderList = ({ orders, onStatusChange, reloadOrders }) => {
  const [statuses, setStatuses] = useState([]);
  const [selectedStatus, setSelectedStatus] = useState({});
  const [editingOrderId, setEditingOrderId] = useState(null);
  const [editOrderData, setEditOrderData] = useState({
    weight: '',
    total_price: '',
    source_location: '',
    destination_location: '',
  });

  useEffect(() => {
    const loadStatuses = async () => {
      const response = await fetchOrderStatuses();
      setStatuses(response.data.statuses);
    };
    loadStatuses();
  }, []);

  const openEditModal = (order) => {
    setEditingOrderId(order.id);
    setEditOrderData({
      weight: order.weight,
      total_price: order.total_price,
      source_location: order.source_location,
      destination_location: order.destination_location,
    });
  };

  const handleEditChange = (e) => {
    const { name, value } = e.target;
    setEditOrderData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  const handleSaveChanges = async () => {
    await updateOrder(editingOrderId, editOrderData);
    reloadOrders();
    setEditingOrderId(null);
  };

  return (
    <div>
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
            <th>Действия</th>
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
                <button onClick={() => onStatusChange(order.id, selectedStatus[order.id])}>
                  Обновить статус
                </button>
              </td>
              <td>
                <button onClick={() => openEditModal(order)}>Изменить</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>

      {editingOrderId && (
        <div className="modal">
          <div className="modal-content">
            <h3>Изменить заказ</h3>
            <label>
              Вес:
              <input
                type="number"
                name="weight"
                value={editOrderData.weight}
                onChange={handleEditChange}
              />
            </label>
            <label>
              Цена:
              <input
                type="number"
                name="total_price"
                value={editOrderData.total_price}
                onChange={handleEditChange}
              />
            </label>
            <label>
              Откуда:
              <input
                type="text"
                name="source_location"
                value={editOrderData.source_location}
                onChange={handleEditChange}
              />
            </label>
            <label>
              Куда:
              <input
                type="text"
                name="destination_location"
                value={editOrderData.destination_location}
                onChange={handleEditChange}
              />
            </label>
            <button onClick={handleSaveChanges}>Сохранить</button>
            <button onClick={() => setEditingOrderId(null)}>Отмена</button>
          </div>
        </div>
      )}
    </div>
  );
};

export default OrderList;