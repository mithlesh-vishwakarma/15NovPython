import React from 'react';

function Playlist({ songs = [] }) {
  if (!songs || songs.length === 0) {
    return <p className="status-msg">Your playlist is empty.</p>;
  }

  return (
    <div className="component-card">
      <h3>1. Playlist Component (List Rendering)</h3>
      <ul className="song-list">
        {songs.map((song, index) => (
          <li key={`${song.title}-${song.artist}-${index}`} className="song-item">
            <span className="song-icon">🎵</span>
            <div className="song-details">
              <strong className="song-title">{song.title}</strong>
              <span className="song-artist">by {song.artist}</span>
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Playlist;

