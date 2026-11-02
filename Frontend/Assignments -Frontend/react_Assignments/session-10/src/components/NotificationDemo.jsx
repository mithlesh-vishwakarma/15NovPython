import React, { useContext } from 'react';
import { NotificationContext } from '../context/NotificationContext';

function NotificationDemo() {
  const { unreadCount, incrementCount, decrementCount, clearCount } =
    useContext(NotificationContext);

  return (
    <div className="component-card">
      <h3>6. WhatsApp-Style Notification Counter Demo</h3>
      <div className="whatsapp-chat-preview">
        <div className="chat-avatar">📱</div>
        <div className="chat-info">
          <strong>Frontend Study Group</strong>
          <p className="chat-snippet">Mithlesh: Check out the new React Context update!</p>
        </div>
        <div className="chat-badge-area">
          <span className="timestamp">14:15</span>
          {unreadCount > 0 && <span className="whatsapp-green-pill">{unreadCount}</span>}
        </div>
      </div>

      <div className="counter-actions">
        <button
          type="button"
          className="btn btn-notify"
          onClick={incrementCount}
        >
          ➕ Receive Message (+1)
        </button>
        <button
          type="button"
          className="btn btn-notify"
          onClick={decrementCount}
          disabled={unreadCount === 0}
        >
          ➖ Mark Message Read (-1)
        </button>
        <button
          type="button"
          className="btn btn-outline"
          onClick={clearCount}
          disabled={unreadCount === 0}
        >
          ✓ Mark All Read (0)
        </button>
      </div>

      <p className="subtext">
        Non-negative safety check: Count cannot drop below 0 (Current: <strong>{unreadCount}</strong>).
      </p>
    </div>
  );
}

export default NotificationDemo;

