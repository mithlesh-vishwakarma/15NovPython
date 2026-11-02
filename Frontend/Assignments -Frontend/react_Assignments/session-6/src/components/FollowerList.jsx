import React from 'react';

function FollowerList({ followers = [] }) {
  return (
    <div className="component-card">
      <h3>3. Follower List (Empty State Handling)</h3>
      {followers.length === 0 ? (
        <p className="status-msg empty-text">No followers yet</p>
      ) : (
        <ul className="followers-list">
          {followers.map((username) => (
            <li key={username} className="follower-item">
              <span className="avatar-placeholder">👤</span>
              <span className="follower-name">@{username}</span>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default FollowerList;

