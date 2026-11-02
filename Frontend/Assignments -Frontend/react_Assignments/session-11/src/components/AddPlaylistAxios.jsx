import React, { useState } from 'react';
import axios from 'axios';

function AddPlaylistAxios() {
  const [playlistName, setPlaylistName] = useState('');
  const [description, setDescription] = useState('');
  const [submitting, setSubmitting] = useState(false);
  const [successInfo, setSuccessInfo] = useState(null);
  const [error, setError] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!playlistName.trim() || !description.trim()) {
      alert('Please fill out both playlist name and description.');
      return;
    }

    try {
      setSubmitting(true);
      setError(null);
      setSuccessInfo(null);

      const response = await axios.post('https://jsonplaceholder.typicode.com/posts', {
        title: playlistName.trim(),
        body: description.trim(),
        userId: 1,
      });

      if (response.status === 201 || response.status === 200) {
        setSuccessInfo({
          id: response.data.id,
          name: response.data.title,
          description: response.data.body,
        });
        setPlaylistName('');
        setDescription('');
      }
    } catch (err) {
      setError(err.message || 'Failed to create playlist');
    } finally {
      setSubmitting(false);
    }
  };

  return (
    <div className="component-card">
      <h3>2. Add Playlist (Axios POST)</h3>
      <p className="subtext">
        Submits new playlist metadata to <code>https://jsonplaceholder.typicode.com/posts</code>.
      </p>

      <form onSubmit={handleSubmit} className="form-stack">
        <div className="form-group">
          <label htmlFor="pl-name">Playlist Name:</label>
          <input
            id="pl-name"
            type="text"
            className="form-control"
            placeholder="e.g. Coding Lofi Beats"
            value={playlistName}
            onChange={(e) => setPlaylistName(e.target.value)}
            disabled={submitting}
          />
        </div>

        <div className="form-group">
          <label htmlFor="pl-desc">Description:</label>
          <textarea
            id="pl-desc"
            className="form-control"
            rows="2"
            placeholder="Chill focus instrumental songs..."
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            disabled={submitting}
          />
        </div>

        <button type="submit" className="btn btn-primary" disabled={submitting}>
          {submitting ? 'Creating...' : '➕ Create Playlist'}
        </button>
      </form>

      {error && <p className="error-alert">Error: {error}</p>}

      {successInfo && (
        <div className="success-banner">
          <h4>✅ Playlist Created Successfully!</h4>
          <p><strong>Simulated ID:</strong> {successInfo.id}</p>
          <p><strong>Name:</strong> {successInfo.name}</p>
          <p><strong>Description:</strong> {successInfo.description}</p>
          <small className="persist-note">
            ℹ️ Note: JSONPlaceholder simulates server creation by returning a fake ID. Real changes are not persisted to a backend database.
          </small>
        </div>
      )}
    </div>
  );
}

export default AddPlaylistAxios;

