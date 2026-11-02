import React from 'react';
import { NavLink } from 'react-router-dom';

function Navbar() {
  const getNavClass = ({ isActive }) =>
    isActive ? 'nav-link active-link' : 'nav-link';

  return (
    <nav className="main-nav" aria-label="Main Navigation">
      <div className="nav-brand">🛒 React Store</div>
      <div className="nav-links">
        <NavLink to="/" end className={getNavClass}>
          Home
        </NavLink>
        <NavLink to="/deals" className={getNavClass}>
          Deals
        </NavLink>
        <NavLink to="/cart" className={getNavClass}>
          Cart
        </NavLink>
      </div>
    </nav>
  );
}

export default Navbar;

