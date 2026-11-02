import React, { useState } from 'react';

function PlaylistAdder() {
  const [songName, setSongName] = useState('');
  const [artist, setArtist] = useState('');
  const [playlist, setPlaylist] = useState([
    { id: 1, songName: 'Calm Down', artist: 'Rema' },
    { id: 2, songName: 'Shape of You', artist: 'Ed Sheeran' },
  ]);

  const handleAddSong = (e) => {
    e.preventDefault();

    if (!songName.trim() || !artist.trim()) {
      return;
    }

    const newTrack = {
      id: Date.now(),
      songName: songName.trim(),
      artist: artist.trim(),
    };

    setPlaylist((prev) => [...prev, newTrack]);
    setSongName('');
    setArtist('');
  };

  return (
    <div className="card">
      <h3>4. Playlist Adder</h3>
      <form onSubmit={handleAddSong} className="form-stack">
        <div className="input-group">
          <label htmlFor="song-name-input" className="form-label">Song Title:</label>
          <input
            id="song-name-input"
            type="text"
            className="form-control"
            placeholder="e.g. Blinding Lights"
            value={songName}
            onChange={(e) => setSongName(e.target.value)}
            required
          />
        </div>

        <div className="input-group">
          <label htmlFor="artist-name-input" className="form-label">Artist Name:</label>
          <input
            id="artist-name-input"
            type="text"
            className="form-control"
            placeholder="e.g. The Weeknd"
            value={artist}
            onChange={(e) => setArtist(e.target.value)}
            required
          />
        </div>

        <button type="submit" className="btn btn-success">
          ➕ Add to Playlist
        </button>
      </form>

      <div className="playlist-display">
        <h4>Current Playlist ({playlist.length} songs)</h4>
        {playlist.length === 0 ? (
          <p className="empty-notice">No songs in playlist yet.</p>
        ) : (
          <ul className="playlist-list">
            {playlist.map((track) => (
              <li key={track.id} className="playlist-item">
                <span className="track-title">🎵 {track.songName}</span>
                <span className="track-artist">— {track.artist}</span>
              </li>
            ))}
          </ul>
        )}
      </div>
    </div>
  );
}

export default PlaylistAdder;

