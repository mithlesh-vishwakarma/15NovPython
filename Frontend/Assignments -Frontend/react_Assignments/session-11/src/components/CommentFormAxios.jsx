import React, { useState } from 'react';
import axios from 'axios';

function CommentFormAxios() {
  const [username, setUsername] = useState('');
  const [comment, setComment] = useState('');
  const [loading, setLoading] = useState(false);
  const [serverReply, setServerReply] = useState(null);
  const [error, setError] = useState(null);

  const handlePostComment = async (e) => {
    e.preventDefault();

    if (!username.trim() || !comment.trim()) {
      alert('Please fill out both username and comment.');
      return;
    }

    try {
      setLoading(true);
      setError(null);
      setServerReply(null);

      const response = await axios.post('https://jsonplaceholder.typicode.com/comments', {
        name: username.trim(),
        email: `${username.trim().toLowerCase().replace(/\s+/g, '.')}@example.com`,
        body: comment.trim(),
        postId: 1,
      });

      if (response.status === 201 || response.status === 200) {
        setServerReply(response.data);
        setUsername('');
        setComment('');
      }
    } catch (err) {
      setError(err.message || 'Error posting comment');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="component-card">
      <h3>4. Submit Comment (Axios POST)</h3>
      <p className="subtext">
        Submits comments to <code>https://jsonplaceholder.typicode.com/comments</code> and displays the returned response.
      </p>

      <form onSubmit={handlePostComment} className="form-stack">
        <div className="form-group">
          <label htmlFor="cmt-user">Username:</label>
          <input
            id="cmt-user"
            type="text"
            className="form-control"
            placeholder="e.g. Mithlesh"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            disabled={loading}
          />
        </div>

        <div className="form-group">
          <label htmlFor="cmt-body">Comment:</label>
          <textarea
            id="cmt-body"
            className="form-control"
            rows="2"
            placeholder="Great discussion on Axios HTTP handling..."
            value={comment}
            onChange={(e) => setComment(e.target.value)}
            disabled={loading}
          />
        </div>

        <button type="submit" className="btn btn-primary" disabled={loading}>
          {loading ? 'Posting...' : '💬 Submit Comment'}
        </button>
      </form>

      {error && <p className="error-alert">Error: {error}</p>}

      {serverReply && (
        <div className="server-response-box">
          <h5>Server Response Returned:</h5>
          <pre>{JSON.stringify(serverReply, null, 2)}</pre>
          <p className="response-summary">
            Post #{serverReply.postId} received comment #{serverReply.id} from <strong>{serverReply.name}</strong>.
          </p>
        </div>
      )}
    </div>
  );
}

export default CommentFormAxios;

