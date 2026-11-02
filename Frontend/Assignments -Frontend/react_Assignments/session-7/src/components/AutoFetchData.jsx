import React, { useState, useEffect } from 'react';

function AutoFetchData() {
  const [posts, setPosts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [refreshIndex, setRefreshIndex] = useState(0);

  useEffect(() => {
    const controller = new AbortController();

    async function fetchData() {
      try {
        setLoading(true);
        setError(null);

        // Auto-fetch on mount refactoring from button trigger
        const res = await fetch('https://jsonplaceholder.typicode.com/posts?_limit=4', {
          signal: controller.signal,
        });

        if (!res.ok) {
          throw new Error(`Failed with status ${res.status}`);
        }

        const data = await res.json();
        setPosts(data);
      } catch (err) {
        if (err.name !== 'AbortError') {
          setError(err.message);
        }
      } finally {
        if (!controller.signal.aborted) {
          setLoading(false);
        }
      }
    }

    fetchData();

    return () => controller.abort();
  }, [refreshIndex]);

  return (
    <div className="component-card">
      <div className="card-top-action">
        <h3>4. Auto-Fetch Refactored Component</h3>
        <button
          type="button"
          className="refresh-btn"
          onClick={() => setRefreshIndex((c) => c + 1)}
          disabled={loading}
        >
          🔄 Refresh
        </button>
      </div>

      <p className="description-text">
        Originally triggered by a manual button click, this component now fetches its initial dataset
        automatically on component mount via <code>useEffect</code> with <code>AbortController</code> lifecycle cleanup.
      </p>

      {loading && <p className="loader">⏳ Fetching posts on mount...</p>}
      {error && <p className="error-alert">Error: {error}</p>}

      {!loading && !error && (
        <div className="posts-grid">
          {posts.map((post) => (
            <div key={post.id} className="post-card">
              <span className="post-num">#{post.id}</span>
              <h5 className="post-heading">{post.title}</h5>
              <p className="post-body">{post.body}</p>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default AutoFetchData;

