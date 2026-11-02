import React from 'react';
import { Link } from 'react-router-dom';

function About() {
  return (
    <div className="page-box">
      <h1>About This Application</h1>
      <p className="lead-text">
        This page is a newly added feature built for Session 13 to verify production bundling and deep-link routing.
      </p>

      <div className="about-details">
        <h3>Architecture Highlights:</h3>
        <ul>
          <li><strong>Framework:</strong> React 18 with modern functional components & hooks</li>
          <li><strong>Build Tool:</strong> Vite 5 producing clean, minified production assets into <code>dist/</code></li>
          <li><strong>Routing:</strong> Client-side routing with <code>react-router-dom</code> v6</li>
          <li><strong>Deployment Strategy:</strong> Netlify redirects rule (<code>/* /index.html 200</code>) for SPA rewrite</li>
        </ul>
      </div>

      <div className="call-to-action">
        <Link to="/products" className="cta-link">Explore Products →</Link>
      </div>
    </div>
  );
}

export default About;

