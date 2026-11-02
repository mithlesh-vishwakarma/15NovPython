import React from 'react';
import LikeButton from './components/LikeButton';
import SearchBar from './components/SearchBar';
import LoginForm from './components/LoginForm';
import PlaylistAdder from './components/PlaylistAdder';
import './index.css';

function App() {
  return (
    <div className="container">
      <header className="page-header">
        <h1>Session 5: Events, Controlled Inputs & Forms</h1>
        <p className="subtitle">
          Handling events, controlled two-way state binding, form submission without page reload, and state lists
        </p>
      </header>

      <main className="grid">
        <LikeButton />
        <SearchBar />
        <LoginForm />
        <PlaylistAdder />
      </main>
    </div>
  );
}

export default App;

