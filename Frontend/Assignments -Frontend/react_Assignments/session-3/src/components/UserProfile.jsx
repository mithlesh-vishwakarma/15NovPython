import React from 'react';
import PropTypes from 'prop-types';

function UserProfile({ username, followers, profilePic }) {
  return (
    <article className="instagram-card">
      <div className="card-header">
        <img
          src={profilePic}
          alt={`${username}'s avatar`}
          className="insta-avatar"
        />
        <div className="user-meta">
          <span className="insta-username">@{username}</span>
          <span className="insta-badge">Verified</span>
        </div>
      </div>
      <div className="follower-stats">
        <span className="stat-number">{followers.toLocaleString('en-IN')}</span>
        <span className="stat-label">followers</span>
      </div>
      <button type="button" className="follow-btn">Follow</button>
    </article>
  );
}

UserProfile.defaultProps = {
  followers: 0,
  profilePic: 'https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?auto=format&fit=crop&w=300&q=80',
};

UserProfile.propTypes = {
  username: PropTypes.string.isRequired,
  followers: PropTypes.number,
  profilePic: PropTypes.string,
};

export default UserProfile;

