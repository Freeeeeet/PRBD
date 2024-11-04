import React from 'react';

const OrderList = ({ orders }) => {
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
                  {status.status_name} — {new Date(status.created_at).toLocaleString()}
                </div>
              ))}
            </td>
          </tr>
        ))}
      </tbody>
    </table>
  );
};

export default OrderList;