import React, { useState, useEffect } from 'react';

function SafeEffectPattern() {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(false);

  useEffect(() => {
    const controller = new AbortController();

    async function loadData() {
      try {
        setLoading(true);
        setError(false);

        const response = await fetch('https://jsonplaceholder.typicode.com/posts', {
          signal: controller.signal,
        });

        if (!response.ok) {
          throw new Error(`HTTP error: ${response.status}`);
        }

        const result = await response.json();
        setData(result.slice(0, 3));
      } catch (err) {
        if (err.name !== 'AbortError') {
          setError(true);
        }
      } finally {
        if (!controller.signal.aborted) {
          setLoading(false);
        }
      }
    }

    loadData();
    return () => controller.abort();
  }, []);

  return (
    <div className="component-card">
      <h3>3. Safe useEffect Pattern Reference Implementation</h3>
      <p className="subtext">
        Demonstrates the correct architectural pattern: HTTP status validation (<code>!response.ok</code>),
        network error catching, AbortController lifecycle cancellation, and safe state dispatch in <code>finally</code>.
      </p>

      {loading && <p className="loading-state">Loading data safely...</p>}
      {error && <div className="error-box"><p className="exact-error-msg">Error loading data</p></div>}

      {!loading && !error && (
        <ul className="songs-list">
          {data.map((item) => (
            <li key={item.id} className="song-row">
              <span className="track-number">Item #{item.id}</span>
              <span className="track-title">{item.title}</span>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default SafeEffectPattern;

