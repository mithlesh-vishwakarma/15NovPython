import React, { useState } from 'react';
import Playlist from './components/Playlist';
import OrderStatus from './components/OrderStatus';
import FollowerList from './components/FollowerList';
import CartSummary from './components/CartSummary';
import './index.css';

function App() {
  const sampleSongs = [
    { title: 'Calm Down', artist: 'Rema' },
    { title: 'Starboy', artist: 'The Weeknd' },
    { title: 'Levitating', artist: 'Dua Lipa' },
  ];

  const populatedFollowers = ['mithlesh_dev', 'coding_ninja', 'react_fanatic'];
  const emptyFollowers = [];

  const cartWithTwoItems = [
    { name: 'Wireless Mouse', price: 899 },
    { name: 'Desk Mat', price: 499 },
  ];

  const cartWithFourItems = [
    { name: 'Wireless Mouse', price: 899 },
    { name: 'Desk Mat', price: 499 },
    { name: 'Mechanical Keyboard', price: 3499 },
    { name: 'USB-C Hub', price: 1299 },
  ];

  const [orderDelivered, setOrderDelivered] = useState(false);
  const [usePopulatedCart, setUsePopulatedCart] = useState(true);

  return (
    <div className="container">
      <header className="page-header">
        <h1>Session 6: Lists and Conditional Rendering</h1>
        <p className="subtitle">
          Mapping arrays, ternary operators, empty states, and conditional UI components
        </p>
      </header>

      <main className="grid">
        <Playlist songs={sampleSongs} />

        <div className="component-card">
          <h3>2. Order Status (Ternary Conditional)</h3>
          <div className="status-demo-box">
            <OrderStatus isDelivered={orderDelivered} orderId="ZOM-9821" />
            <button
              type="button"
              className="toggle-btn"
              onClick={() => setOrderDelivered((prev) => !prev)}
            >
              Toggle Status (Currently: {orderDelivered ? 'Delivered' : 'On the way'})
            </button>
          </div>
        </div>

        <FollowerList followers={populatedFollowers} />
        <FollowerList followers={emptyFollowers} />

        <div className="cart-demo-wrapper">
          <div className="cart-controls">
            <button
              type="button"
              className={`filter-btn ${usePopulatedCart ? 'active' : ''}`}
              onClick={() => setUsePopulatedCart(true)}
            >
              Demo Cart (4 items - Eligible for Checkout)
            </button>
            <button
              type="button"
              className={`filter-btn ${!usePopulatedCart ? 'active' : ''}`}
              onClick={() => setUsePopulatedCart(false)}
            >
              Demo Cart (2 items - Under threshold)
            </button>
          </div>
          <CartSummary items={usePopulatedCart ? cartWithFourItems : cartWithTwoItems} />
          <CartSummary items={[]} />
        </div>
      </main>
    </div>
  );
}

export default App;

