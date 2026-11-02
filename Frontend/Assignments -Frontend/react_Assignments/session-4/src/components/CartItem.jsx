import React, { useState } from 'react';

function CartItem({ itemName = 'Wireless Earbuds' }) {
  const [quantity, setQuantity] = useState(1);

  const increment = () => {
    setQuantity((prev) => prev + 1);
  };

  const decrement = () => {
    setQuantity((prev) => (prev > 0 ? prev - 1 : 0));
  };

  return (
    <div className="exercise-card">
      <h3>2. Cart Item Quantity</h3>
      <div className="cart-row">
        <span className="item-name">{itemName}</span>
        <div className="quantity-controls">
          <button
            type="button"
            className="qty-btn"
            onClick={decrement}
            disabled={quantity === 0}
            aria-label="Decrease quantity"
          >
            -
          </button>
          <span className="qty-display">{quantity}</span>
          <button
            type="button"
            className="qty-btn"
            onClick={increment}
            aria-label="Increase quantity"
          >
            +
          </button>
        </div>
      </div>
      {quantity === 0 && <p className="helper-text muted">Item removed from active cart</p>}
    </div>
  );
}

export default CartItem;

