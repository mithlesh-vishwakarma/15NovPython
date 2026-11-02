import React from 'react';
import LikeButton from './components/LikeButton';
import CartItem from './components/CartItem';
import SongVote from './components/SongVote';
import StarRating from './components/StarRating';
import './index.css';

function App() {
  return (
    <div className="container">
      <header className="header">
        <h1>Session 4: useState Interaction Exercises</h1>
        <p className="subtitle">State management with interactive event handlers and conditional limits</p>
      </header>

      <div className="grid">
        <LikeButton />
        <CartItem itemName="Sony WH-1000XM5 Headphones" />
        <SongVote songTitle="Calm Down - Rema" />
        <StarRating totalStars={5} />
      </div>
    </div>
  );
}

export default App;

