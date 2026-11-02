import React from 'react';
import AutoFocusSearchBar from './components/AutoFocusSearchBar';
import RefLoginForm from './components/RefLoginForm';
import AddToPlaylistRef from './components/AddToPlaylistRef';
import FeedbackFormRef from './components/FeedbackFormRef';
import './index.css';

function App() {
  return (
    <div className="container">
      <header className="page-header">
        <h1>Session 8: useRef & Controlled Forms</h1>
        <p className="subtitle">
          Direct DOM element references, auto-focus on mount, post-submit cursor placement, and focus buttons
        </p>
      </header>

      <main className="content-stack">
        <AutoFocusSearchBar />
        <RefLoginForm />
        <AddToPlaylistRef />
        <FeedbackFormRef />
      </main>
    </div>
  );
}

export default App;

