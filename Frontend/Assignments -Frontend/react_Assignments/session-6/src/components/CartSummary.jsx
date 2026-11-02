import React from 'react';

function CartSummary({ items = [] }) {
  if (items.length === 0) {
    return (
      <div className="component-card">
        <h3>4. Cart Summary</h3>
        <p className="status-msg empty-text">Cart is empty</p>
      </div>
    );
  }

  const totalPrice = items.reduce((sum, item) => sum + (item.price || 0), 0);
  const eligibleForCheckout = items.length >= 3;

  return (
    <div className="component-card">
      <h3>4. Cart Summary ({items.length} items)</h3>
      <ul className="cart-items-list">
        {items.map((item, index) => (
          <li key={`${item.name}-${index}`} className="cart-item-row">
            <span className="cart-item-name">{item.name}</span>
            <span className="cart-item-price">₹{item.price.toLocaleString('en-IN')}</span>
          </li>
        ))}
      </ul>

      <div className="cart-total-row">
        <strong>Total Amount:</strong>
        <strong>₹{totalPrice.toLocaleString('en-IN')}</strong>
      </div>

      {eligibleForCheckout ? (
        <button type="button" className="checkout-btn">
          Checkout Now ({items.length} items)
        </button>
      ) : (
        <p className="checkout-notice">
          <em>Add at least {3 - items.length} more item(s) to unlock "Checkout Now" (minimum 3 items required).</em>
        </p>
      )}
    </div>
  );
}

export default CartSummary;

