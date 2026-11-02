import React, { useRef, useEffect, useState } from 'react';

function AutoFocusSearchBar() {
  const inputRef = useRef(null);
  const [query, setQuery] = useState('');

  useEffect(() => {
    // Focus the input automatically after mount safely
    if (inputRef.current) {
      inputRef.current.focus();
    }
  }, []);

  const handleSearch = (e) => {
    e.preventDefault();
    if (query.trim()) {
      alert(`Searching for: "${query}"`);
    } else if (inputRef.current) {
      inputRef.current.focus();
    }
  };

  return (
    <div className="component-card">
      <h3>1. Auto-Focus Search Bar</h3>
      <p className="subtext">The input below was automatically focused upon component mounting via <code>useRef</code>.</p>
      <form onSubmit={handleSearch} className="inline-form">
        <input
          ref={inputRef}
          type="text"
          className="form-control"
          placeholder="Search products, songs, movies..."
          value={query}
          onChange={(e) => setQuery(e.target.value)}
        />
        <button type="submit" className="btn btn-primary">
          🔍 Search
        </button>
      </form>
    </div>
  );
}

export default AutoFocusSearchBar;

