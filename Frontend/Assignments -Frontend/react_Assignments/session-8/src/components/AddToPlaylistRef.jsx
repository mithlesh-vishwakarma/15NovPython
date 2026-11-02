import React, { useState, useRef } from 'react';

function AddToPlaylistRef() {
  const [songName, setSongName] = useState('');
  const [playlist, setPlaylist] = useState(['Calm Down', 'Blinding Lights']);
  const songInputRef = useRef(null);

  const handleAddSong = (e) => {
    e.preventDefault();

    const trimmed = songName.trim();
    if (!trimmed) {
      if (songInputRef.current) songInputRef.current.focus();
      return;
    }

    // Add to displayed playlist
    setPlaylist((prev) => [...prev, trimmed]);

    // Clear input
    setSongName('');

    // Re-focus input field
    if (songInputRef.current) {
      songInputRef.current.focus();
    }
  };

  return (
    <div className="component-card">
      <h3>3. Add to Playlist (Rapid Entry with Auto-Focus)</h3>
      <form onSubmit={handleAddSong} className="inline-form">
        <input
          ref={songInputRef}
          type="text"
          className="form-control"
          placeholder="Enter next track name..."
          value={songName}
          onChange={(e) => setSongName(e.target.value)}
        />
        <button type="submit" className="btn btn-success">
          ➕ Add Track
        </button>
      </form>

      <ul className="simple-list">
        {playlist.map((song, idx) => (
          <li key={`${song}-${idx}`} className="list-item">
            🎵 {song}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default AddToPlaylistRef;

