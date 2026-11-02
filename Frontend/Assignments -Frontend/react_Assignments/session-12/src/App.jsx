import React from 'react';
import TrendingSongsFetch from './components/TrendingSongsFetch';
import IPLScoresFetch from './components/IPLScoresFetch';
import SafeEffectPattern from './components/SafeEffectPattern';
import './index.css';

function App() {
  return (
    <div className="container">
      <header className="page-header">
        <h1>Session 12: Fetch, Reload, Status Handling & Errors</h1>
        <p className="subtitle">
          Reliable asynchronous lifecycle management, explicit HTTP status checks, retry mechanisms, and AbortController cleanup
        </p>
      </header>

      <main className="content-stack">
        <TrendingSongsFetch />
        <IPLScoresFetch />
        <SafeEffectPattern />
      </main>
    </div>
  );
}

export default App;

