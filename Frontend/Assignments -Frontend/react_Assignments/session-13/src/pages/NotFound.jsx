import React from 'react';
import { Link } from 'react-router-dom';

function NotFound() {
  return (
    <div className="page-box not-found-center">
      <h1>404 - Page Not Found</h1>
      <p>The page you requested could not be found.</p>
      <Link to="/" className="cta-link">Back to Homepage</Link>
    </div>
  );
}

export default NotFound;

