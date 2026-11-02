import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import HomePage from './pages/HomePage';
import DealsPage from './pages/DealsPage';
import CartPage from './pages/CartPage';
import NotFound from './pages/NotFound';
import './index.css';

function App() {
  return (
    <div className="app-layout">
      <Navbar />
      <main className="main-content">
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/deals" element={<DealsPage />} />
          <Route path="/cart" element={<CartPage />} />
          <Route path="*" element={<NotFound />} />
        </Routes>
      </main>
    </div>
  );
}

export default App;

