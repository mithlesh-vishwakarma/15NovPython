import React from 'react';

function ProfileCard({
  name = 'Mithlesh',
  profilePictureUrl = 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=320&q=80',
  bio = 'Passionate Frontend & React Developer building intuitive, accessible web interfaces.',
}) {
  return (
    <article className="profile-card">
      <div className="avatar-wrapper">
        <img
          src={profilePictureUrl}
          alt={`${name}'s profile avatar`}
          className="profile-img"
        />
      </div>
      <h2 className="profile-name">{name}</h2>
      <p className="profile-bio">{bio}</p>
    </article>
  );
}

export default ProfileCard;

