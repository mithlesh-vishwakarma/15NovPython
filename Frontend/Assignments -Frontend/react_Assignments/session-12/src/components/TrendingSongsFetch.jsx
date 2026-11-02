import React, { useState, useEffect } from 'react';

function TrendingSongsFetch() {
  const [songs, setSongs] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(false);
  const [reloadTrigger, setReloadTrigger] = useState(0);
  const [simulateFailure, setSimulateFailure] = useState(false);

  useEffect(() => {
    const controller = new AbortController();

    async function fetchTrendingSongs() {
      try {
        setLoading(true);
        setError(false);

        const targetUrl = simulateFailure
          ? 'https://invalid-nonexistent-domain-404.xyz/error'
          : 'https://jsonplaceholder.typicode.com/posts';

        const response = await fetch(targetUrl, { signal: controller.signal });

        if (!response.ok) {
          throw new Error(`HTTP error: ${response.status}`);
        }

        const data = await response.json();
        setSongs(data.slice(0, 3));
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

    fetchTrendingSongs();

    return () => controller.abort();
  }, [reloadTrigger, simulateFailure]);

  const handleReload = () => {
    setReloadTrigger((count) => count + 1);
  };

  return (
    <div className="component-card">
      <div className="card-top-bar">
        <h3>1. Trending Songs (Fetch API)</h3>
        <div className="btn-actions">
          <button
            type="button"
            className="btn btn-secondary"
            onClick={() => setSimulateFailure((prev) => !prev)}
          >
            {simulateFailure ? 'Mode: Simulated Failure ⚠️' : 'Mode: Normal Online'}
          </button>
          <button
            type="button"
            className="btn btn-primary"
            onClick={handleReload}
            disabled={loading}
          >
            🔄 Reload
          </button>
        </div>
      </div>

      <p className="subtext">
        Fetches the first three song titles. If the request fails, displays the exact requested message:
        <code>Error loading data</code>.
      </p>

      {loading && <p className="loading-state">Loading songs...</p>}

      {error ? (
        <div className="error-box" role="alert">
          <p className="exact-error-msg">Error loading data</p>
        </div>
      ) : (
        !loading && (
          <ul className="songs-list">
            {songs.map((song) => (
              <li key={song.id} className="song-row">
                <span className="track-number">#{song.id}</span>
                <span className="track-title">{song.title}</span>
              </li>
            ))}
          </ul>
        )
      )}
    </div>
  );
}

export default TrendingSongsFetch;

