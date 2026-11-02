import React, { useState, useEffect } from 'react';

function IPLScoresFetch() {
  const [scores, setScores] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(false);
  const [simulateError, setSimulateError] = useState(false);

  useEffect(() => {
    const controller = new AbortController();

    async function loadIPLScores() {
      try {
        setLoading(true);
        setError(false);

        const url = simulateError
          ? 'https://jsonplaceholder.typicode.com/invalid_404_url'
          : 'https://jsonplaceholder.typicode.com/users';

        const response = await fetch(url, { signal: controller.signal });

        // Check response.ok before parsing
        if (!response.ok) {
          throw new Error(`HTTP error: ${response.status}`);
        }

        const data = await response.json();
        // Transform dummy users into mock cricket match scorecards
        const mockScorecards = data.slice(0, 4).map((user, idx) => ({
          id: user.id,
          teamA: `Team ${user.name.split(' ')[0]}`,
          teamB: `Team ${user.company.name.split(' ')[0]}`,
          scoreA: `${140 + idx * 12}/${3 + (idx % 4)} (20.0)`,
          scoreB: `${135 + idx * 8}/${5 + (idx % 5)} (19.4)`,
          status: idx % 2 === 0 ? 'Match Completed' : 'In Progress',
        }));

        setScores(mockScorecards);
      } catch (err) {
        if (err.name !== 'AbortError') {
          // Exact error state per requirement
          setError(true);
        }
      } finally {
        if (!controller.signal.aborted) {
          setLoading(false);
        }
      }
    }

    loadIPLScores();

    return () => controller.abort();
  }, [simulateError]);

  return (
    <div className="component-card">
      <div className="card-top-bar">
        <h3>2. IPL Scores (HTTP Status Checking)</h3>
        <button
          type="button"
          className="btn btn-secondary"
          onClick={() => setSimulateError((p) => !p)}
        >
          {simulateError ? 'Reset to Valid URL' : 'Simulate HTTP 404'}
        </button>
      </div>

      <div className="disclaimer-banner">
        ⚠️ <strong>Notice:</strong> This is mock cricket data mapped from JSONPlaceholder users for educational demonstration, not live scores.
      </div>

      {loading && <p className="loading-state">Loading scorecards...</p>}

      {error ? (
        <div className="error-box" role="alert">
          <p className="exact-error-msg">Error loading scores</p>
        </div>
      ) : (
        !loading && (
          <div className="match-grid">
            {scores.map((match) => (
              <div key={match.id} className="match-card">
                <div className="match-status-tag">{match.status}</div>
                <div className="team-row">
                  <span className="team-name">{match.teamA}</span>
                  <span className="team-score">{match.scoreA}</span>
                </div>
                <div className="team-row">
                  <span className="team-name">{match.teamB}</span>
                  <span className="team-score">{match.scoreB}</span>
                </div>
              </div>
            ))}
          </div>
        )
      )}
    </div>
  );
}

export default IPLScoresFetch;

