import React from 'react';
import { Link } from 'react-router-dom';

function NotFound() {
  return (
    <div className="page-content not-found-page">
      <h2>404 - Page Not Found</h2>
      <p>The page you are looking for does not exist or has been moved.</p>
      <Link to="/" className="cta-button">Return to Home</Link>
    </div>
  );
}

export default NotFound;

