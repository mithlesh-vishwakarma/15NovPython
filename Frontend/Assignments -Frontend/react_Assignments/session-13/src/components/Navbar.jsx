import React from 'react';
import { NavLink } from 'react-router-dom';

function Navbar({ darkMode, setDarkMode }) {
  const getNavClass = ({ isActive }) =>
    isActive ? 'nav-link active' : 'nav-link';

  return (
    <nav className="site-navbar" aria-label="Main Navigation">
      <div className="nav-container">
        <span className="brand-logo">🚀 DeployPro</span>

        <div className="nav-links">
          <NavLink to="/" end className={getNavClass}>Home</NavLink>
          <NavLink to="/products" className={getNavClass}>Products</NavLink>
          <NavLink to="/about" className={getNavClass}>About Us</NavLink>
        </div>

        <button
          type="button"
          className="theme-btn"
          onClick={() => setDarkMode((prev) => !prev)}
          aria-label="Toggle dark mode"
        >
          {darkMode ? '☀️ Light' : '🌙 Dark'}
        </button>
      </div>
    </nav>
  );
}

export default Navbar;

