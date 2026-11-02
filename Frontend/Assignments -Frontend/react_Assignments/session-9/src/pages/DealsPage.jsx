import React from 'react';
import { Link } from 'react-router-dom';

function DealsPage() {
  const deals = [
    { id: 1, name: 'Sony WH-1000XM5 Wireless Headphones', original: 29999, discount: 22999 },
    { id: 2, name: 'Logitech MX Master 3S Mouse', original: 9999, discount: 7499 },
    { id: 3, name: 'Keychron K2 Mechanical Keyboard', original: 8499, discount: 6499 },
  ];

  return (
    <div className="page-content">
      <h2>🔥 Exclusive Today Deals</h2>
      <div className="deals-grid">
        {deals.map((deal) => (
          <div key={deal.id} className="deal-card">
            <h4>{deal.name}</h4>
            <div className="deal-prices">
              <span className="discount-price">₹{deal.discount.toLocaleString('en-IN')}</span>
              <span className="orig-price">₹{deal.original.toLocaleString('en-IN')}</span>
            </div>
            <Link to="/cart" className="add-cart-link">Add to Cart →</Link>
          </div>
        ))}
      </div>
    </div>
  );
}

export default DealsPage;

