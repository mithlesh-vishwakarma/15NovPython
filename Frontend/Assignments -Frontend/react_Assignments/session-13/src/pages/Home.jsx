import React from 'react';
import { Link } from 'react-router-dom';

function Home() {
  return (
    <div className="page-box">
      <h1>Production Ready Single Page Application</h1>
      <p className="lead-text">
        Demonstrating build optimization, Netlify SPA redirect rules, responsive design, and dynamic theme switching.
      </p>

      <div className="feature-grid">
        <div className="feature-card">
          <h3>⚡ High Performance</h3>
          <p>Bundled with Vite for instant loading, CSS code splitting, and gzip-compressed asset delivery.</p>
        </div>
        <div className="feature-card">
          <h3>🌐 Netlify SPA Ready</h3>
          <p>Configured with <code>public/_redirects</code> to prevent 404 errors on deep linking and browser reloads.</p>
        </div>
        <div className="feature-card">
          <h3>🎨 Interactive Theme</h3>
          <p>Built-in light/dark mode with CSS custom properties and instant switching.</p>
        </div>
      </div>

      <div className="call-to-action">
        <Link to="/about" className="cta-link">Learn About This App →</Link>
      </div>
    </div>
  );
}

export default Home;

