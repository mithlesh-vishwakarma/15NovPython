import React, { useState, useEffect } from 'react';

function MovieSuggestions() {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const controller = new AbortController();

    async function loadSuggestions() {
      try {
        setLoading(true);
        setError(null);

        const response = await fetch('https://jsonplaceholder.typicode.com/users', {
          signal: controller.signal,
        });

        if (!response.ok) {
          throw new Error(`HTTP Error: ${response.status} ${response.statusText}`);
        }

        const data = await response.json();
        setUsers(data);
      } catch (err) {
        if (err.name !== 'AbortError') {
          setError(err.message || 'Unable to retrieve movie suggestions at this time.');
        }
      } finally {
        if (!controller.signal.aborted) {
          setLoading(false);
        }
      }
    }

    loadSuggestions();

    return () => controller.abort();
  }, []);

  return (
    <div className="component-card">
      <h3>3. Movie Enthusiast Suggestions (Data Fetch)</h3>

      {loading && <p className="loader">🎬 Loading movie recommendations...</p>}

      {error && (
        <div className="error-alert">
          <p>⚠️ <strong>Request Failed:</strong> {error}</p>
        </div>
      )}

      {!loading && !error && (
        <ul className="items-list">
          {users.map((user) => (
            <li key={user.id} className="item-row">
              <span className="movie-icon">🎥</span>
              <div className="item-meta">
                <strong>{user.name}</strong>
                <span className="item-sub">Curator handle: @{user.username}</span>
              </div>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default MovieSuggestions;

