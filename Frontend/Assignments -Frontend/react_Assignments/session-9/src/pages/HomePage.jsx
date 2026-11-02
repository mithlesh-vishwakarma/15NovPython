import React from 'react';
import { Link } from 'react-router-dom';

function HomePage() {
  return (
    <div className="page-content">
      <h2>🏠 Welcome to React Store Home</h2>
      <p>Discover top tech accessories, premium headphones, and exclusive deals!</p>

      <div className="banner-cta">
        <h3>Super Festive Electronics Sale!</h3>
        <p>Save up to 40% on noise-cancelling headphones and accessories.</p>
        <Link to="/deals" className="cta-button">Browse Deals Now →</Link>
      </div>
    </div>
  );
}

export default HomePage;

