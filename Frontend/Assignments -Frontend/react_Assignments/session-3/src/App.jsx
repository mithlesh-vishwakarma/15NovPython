import React from 'react';
import ProductCard from './components/ProductCard';
import UserProfile from './components/UserProfile';
import './index.css';

function App() {
  return (
    <div className="container">
      <header className="page-header">
        <h1>Props, Default Props & PropTypes Validation</h1>
      </header>

      <section className="section-block">
        <h2>1. Product Cards (with PropTypes Validation)</h2>
        <div className="card-grid">
          <ProductCard productName="Wireless Noise-Cancelling Headphones" price={14999} />
          <ProductCard productName="Mechanical Gaming Keyboard RGB" price={4499} />
        </div>
      </section>

      <section className="section-block">
        <h2>2. User Profiles (with Default Props Demo)</h2>
        <div className="card-grid">
          <div className="demo-item">
            <p className="item-label">Full Props Provided:</p>
            <UserProfile
              username="alex_codes"
              followers={12450}
              profilePic="https://images.unsplash.com/photo-1570295999919-56ceb5ecca61?auto=format&fit=crop&w=300&q=80"
            />
          </div>

          <div className="demo-item">
            <p className="item-label">Default Props Fallback (no followers & no pic provided):</p>
            <UserProfile username="new_developer" />
          </div>
        </div>
      </section>
    </div>
  );
}

export default App;

