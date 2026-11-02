import React, { useContext } from 'react';
import { UserContext } from '../context/UserContext';
import { ThemeContext } from '../context/ThemeContext';
import { NotificationContext } from '../context/NotificationContext';

function Navbar() {
  const { username, loggedIn, toggleLogin } = useContext(UserContext);
  const { theme, toggleTheme } = useContext(ThemeContext);
  const { unreadCount } = useContext(NotificationContext);

  return (
    <header className="navbar-header">
      <div className="brand">⚛️ ContextStore</div>

      <div className="nav-controls">
        <div className="user-status">
          👤 <span>{loggedIn ? username : 'Guest'}</span>
          <button
            type="button"
            className="btn-status-toggle"
            onClick={toggleLogin}
            aria-label="Toggle user login state"
          >
            {loggedIn ? 'Log out' : 'Log in'}
          </button>
        </div>

        <div className="notification-icon-wrap" title="Unread notifications">
          💬 Messages
          {unreadCount > 0 && <span className="whatsapp-badge">{unreadCount}</span>}
        </div>

        <button
          type="button"
          className="btn-theme-toggle"
          onClick={toggleTheme}
          aria-label="Toggle theme"
        >
          {theme === 'light' ? '🌙 Dark Mode' : '☀️ Light Mode'}
        </button>
      </div>
    </header>
  );
}

export default Navbar;

