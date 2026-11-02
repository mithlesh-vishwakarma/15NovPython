import React from 'react';
import { Link } from 'react-router-dom';

function CartPage() {
  return (
    <div className="page-content">
      <h2>🛍️ Your Shopping Cart</h2>
      <div className="cart-empty-notice">
        <p>Your cart currently has <strong>1 promotional item</strong>:</p>
        <div className="cart-demo-item">
          <span>🎧 Sony WH-1000XM5 (Black)</span>
          <strong>₹22,999</strong>
        </div>
        <Link to="/deals" className="continue-link">← Keep Shopping</Link>
      </div>
    </div>
  );
}

export default CartPage;

