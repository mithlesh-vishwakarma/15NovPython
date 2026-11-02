import React from 'react';
import PopularMoviesAxios from './components/PopularMoviesAxios';
import AddPlaylistAxios from './components/AddPlaylistAxios';
import RestaurantSearchAxios from './components/RestaurantSearchAxios';
import CommentFormAxios from './components/CommentFormAxios';
import './index.css';

function App() {
  return (
    <div className="container">
      <header className="page-header">
        <h1>Session 11: Axios GET, POST, Search & Request States</h1>
        <p className="subtitle">
          Handling REST requests with Axios, request cancellations, simulated POST responses, and client-side filtering
        </p>
      </header>

      <main className="content-stack">
        <PopularMoviesAxios />
        <AddPlaylistAxios />
        <RestaurantSearchAxios />
        <CommentFormAxios />
      </main>
    </div>
  );
}

export default App;

