import React from 'react';
import TrendingSongs from './components/TrendingSongs';
import IPLScoreFetcher from './components/IPLScoreFetcher';
import MovieSuggestions from './components/MovieSuggestions';
import AutoFetchData from './components/AutoFetchData';
import './index.css';

function App() {
  return (
    <div className="container">
      <header className="page-header">
        <h1>Session 7: useEffect and Data Fetching</h1>
        <p className="subtitle">
          Mount lifecycles, HTTP response checking, async data fetching, and AbortController cleanup
        </p>
      </header>

      <main className="content-stack">
        <TrendingSongs />
        <IPLScoreFetcher />
        <MovieSuggestions />
        <AutoFetchData />
      </main>
    </div>
  );
}

export default App;

