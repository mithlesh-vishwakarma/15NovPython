import React from 'react';

function MiniProfile({
  name = 'Mithlesh',
  status = 'Learning React & building awesome frontend apps 🚀',
  imageUrl = 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=300&q=80'
}) {
  return (
    <div className="mini-profile-card">
      <img
        src={imageUrl}
        alt={`${name}'s profile avatar`}
        className="profile-avatar"
      />
      <h3 className="profile-name">{name}</h3>
      <p className="profile-status">{status}</p>
    </div>
  );
}

export default MiniProfile;

