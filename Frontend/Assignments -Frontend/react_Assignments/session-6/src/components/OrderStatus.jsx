import React from 'react';

function OrderStatus({ isDelivered, orderId }) {
  return (
    <div className={`status-badge ${isDelivered ? 'delivered' : 'pending'}`}>
      {orderId && <span className="order-tag">Order #{orderId}: </span>}
      <span className="status-text">
        {isDelivered ? 'Order Delivered 🎉' : 'Order on the way 🚚'}
      </span>
    </div>
  );
}

export default OrderStatus;

