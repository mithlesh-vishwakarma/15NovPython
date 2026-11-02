import React, { useState, useEffect } from 'react';

function IPLScoreFetcher() {
  const [headline, setHeadline] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const controller = new AbortController();

    async function fetchMatchHeadline() {
      try {
        setLoading(true);
        setError(null);

        const response = await fetch('https://jsonplaceholder.typicode.com/posts', {
          signal: controller.signal,
        });

        if (!response.ok) {
          throw new Error(`Server returned HTTP ${response.status}`);
        }

        const data = await response.json();
        if (data && data.length > 0) {
          setHeadline(data[0].title);
        } else {
          setHeadline('No match headlines available');
        }
      } catch (err) {
        if (err.name !== 'AbortError') {
          setError(err.message || 'Failed to fetch match headline');
        }
      } finally {
        if (!controller.signal.aborted) {
          setLoading(false);
        }
      }
    }

    fetchMatchHeadline();

    return () => controller.abort();
  }, []);

  return (
    <div className="component-card">
      <div className="header-with-badge">
        <h3>2. IPL Score & Match Headline</h3>
        <span className="mock-badge">⚠️ Simulated Mock Data</span>
      </div>

      <p className="mock-disclaimer">
        <em>Note: This is simulated placeholder data from JSONPlaceholder for assignment purposes, not real live IPL match scores.</em>
      </p>

      {loading && <div className="loader">🏏 Loading match headline...</div>}
      {error && <div className="error-alert">Error loading headline: {error}</div>}
      {!loading && !error && (
        <div className="headline-box">
          <span className="live-pill">🔴 MATCH UPDATE</span>
          <h4 className="headline-text">"{headline}"</h4>
          <p className="score-summary">CSK: 188/4 (20.0) | RCB: 176/8 (20.0) — CSK won by 12 runs</p>
        </div>
      )}
    </div>
  );
}

export default IPLScoreFetcher;

