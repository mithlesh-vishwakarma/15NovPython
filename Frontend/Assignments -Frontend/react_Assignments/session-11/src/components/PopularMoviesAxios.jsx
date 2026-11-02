import React, { useState, useEffect } from 'react';
import axios from 'axios';

function PopularMoviesAxios() {
  const [movies, setMovies] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    let isMounted = true;
    const source = axios.CancelToken.source();

    async function fetchMovies() {
      try {
        setLoading(true);
        setError(null);

        // Per assignment: Using approved mock alternative if TMDB API key is not configured
        const response = await axios.get('https://jsonplaceholder.typicode.com/posts', {
          cancelToken: source.token,
          params: { _limit: 5 },
        });

        if (response.status !== 200) {
          throw new Error(`Unexpected status code: ${response.status}`);
        }

        if (isMounted) {
          setMovies(response.data.slice(0, 5));
        }
      } catch (err) {
        if (!axios.isCancel(err) && isMounted) {
          setError(err.message || 'Failed to load movie suggestions.');
        }
      } finally {
        if (isMounted) {
          setLoading(false);
        }
      }
    }

    fetchMovies();

    return () => {
      isMounted = false;
      source.cancel('Component unmounted');
    };
  }, []);

  return (
    <div className="component-card">
      <div className="card-header-flex">
        <h3>1. Popular Movies (Axios GET)</h3>
        <span className="badge-mock">Mock Data Fallback</span>
      </div>

      <p className="notice-text">
        <em>Fetched via Axios using JSONPlaceholder mock endpoint (first 5 items).</em>
      </p>

      {loading && <p className="loading-state">Loading...</p>}

      {error && (
        <div className="error-alert">
          <p>⚠️ Error loading movies: {error}</p>
        </div>
      )}

      {!loading && !error && (
        <ol className="movie-list">
          {movies.map((item) => (
            <li key={item.id} className="movie-item">
              <span className="movie-tag">Movie #{item.id}</span>
              <strong className="movie-title">{item.title}</strong>
            </li>
          ))}
        </ol>
      )}
    </div>
  );
}

export default PopularMoviesAxios;

