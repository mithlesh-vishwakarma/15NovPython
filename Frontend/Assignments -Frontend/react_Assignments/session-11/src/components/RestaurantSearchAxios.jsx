import React, { useState, useEffect } from 'react';
import axios from 'axios';

const FALLBACK_RESTAURANTS = [
  { id: 1, name: 'Bawarchi Biryani', cuisine: 'Hyderabadi Mughlai', rating: 4.6, city: 'Hyderabad' },
  { id: 2, name: 'Punjab Grill', cuisine: 'North Indian & Tandoori', rating: 4.4, city: 'Delhi' },
  { id: 3, name: 'Paradise Food Court', cuisine: 'Biryani & Kebab', rating: 4.2, city: 'Bangalore' },
  { id: 4, name: 'Dakshin Samrat', cuisine: 'South Indian Coastal', rating: 4.5, city: 'Chennai' },
  { id: 5, name: 'Pizza Bellissimo', cuisine: 'Italian Woodfire Pizza', rating: 4.3, city: 'Mumbai' },
  { id: 6, name: 'Sushi Zen Garden', cuisine: 'Japanese Sushi & Ramen', rating: 4.7, city: 'Pune' },
  { id: 7, name: 'The Burger Barn', cuisine: 'American Burgers & Fries', rating: 4.1, city: 'Goa' },
];

function RestaurantSearchAxios() {
  const [restaurants, setRestaurants] = useState([]);
  const [searchTerm, setSearchTerm] = useState('');
  const [loading, setLoading] = useState(true);
  const [usingFallback, setUsingFallback] = useState(false);

  useEffect(() => {
    let active = true;

    async function loadRestaurants() {
      try {
        setLoading(true);
        // Attempting remote mock endpoint
        const res = await axios.get('https://mocki.io/v1/d4867d8b-b5d5-4a48-a4ab-79131b5809b8', {
          timeout: 2500,
        });
        if (active && res.data && Array.isArray(res.data) && res.data.length > 0) {
          setRestaurants(res.data);
        } else {
          throw new Error('Remote mock data empty');
        }
      } catch (err) {
        // Fallback gracefully to reliable local mock restaurant dataset per assignment requirements
        if (active) {
          setRestaurants(FALLBACK_RESTAURANTS);
          setUsingFallback(true);
        }
      } finally {
        if (active) {
          setLoading(false);
        }
      }
    }

    loadRestaurants();

    return () => {
      active = false;
    };
  }, []);

  const filtered = restaurants.filter((r) =>
    r.name.toLowerCase().includes(searchTerm.toLowerCase().trim())
  );

  return (
    <div className="component-card">
      <div className="card-header-flex">
        <h3>3. Restaurant Search (Live Filtering)</h3>
        {usingFallback && <span className="badge-demo">Demo Dataset Active</span>}
      </div>

      <p className="notice-text">
        <em>Filter restaurant names case-insensitively in real-time as you type.</em>
      </p>

      <div className="search-box-wrap">
        <input
          type="text"
          className="form-control"
          placeholder="Filter restaurants (e.g. Biryani, Pizza, Punjab)..."
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
        />
        {searchTerm && (
          <button
            type="button"
            className="clear-search-btn"
            onClick={() => setSearchTerm('')}
            aria-label="Clear search"
          >
            ✕
          </button>
        )}
      </div>

      {loading && <p className="loading-state">Loading restaurants...</p>}

      {!loading && (
        <div className="restaurant-results">
          {filtered.length === 0 ? (
            <div className="empty-state">
              <span className="empty-icon">🍽️</span>
              <p>No restaurants match "<strong>{searchTerm}</strong>".</p>
              <button
                type="button"
                className="btn btn-secondary"
                onClick={() => setSearchTerm('')}
              >
                Reset Search Filter
              </button>
            </div>
          ) : (
            <ul className="restaurant-grid">
              {filtered.map((item) => (
                <li key={item.id} className="restaurant-card">
                  <div className="resto-header">
                    <h4>{item.name}</h4>
                    <span className="rating-pill">⭐ {item.rating}</span>
                  </div>
                  <p className="cuisine-line">{item.cuisine}</p>
                  <span className="city-pill">📍 {item.city}</span>
                </li>
              ))}
            </ul>
          )}
        </div>
      )}
    </div>
  );
}

export default RestaurantSearchAxios;

