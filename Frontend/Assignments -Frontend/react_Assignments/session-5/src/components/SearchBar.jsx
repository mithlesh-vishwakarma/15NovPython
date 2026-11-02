import React, { useState } from 'react';

function SearchBar() {
  const [searchTerm, setSearchTerm] = useState('');

  return (
    <div className="card">
      <h3>2. Controlled Search Bar</h3>
      <div className="input-group">
        <label htmlFor="search-input" className="form-label">Search Keyword:</label>
        <input
          id="search-input"
          type="text"
          className="form-control"
          placeholder="Type to search (e.g. Biryani, Pizza)..."
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
        />
      </div>
      <div className="live-preview">
        <strong>Current input:</strong>{' '}
        <span className="preview-text">
          {searchTerm ? searchTerm : <em>(waiting for user input...)</em>}
        </span>
      </div>
    </div>
  );
}

export default SearchBar;

