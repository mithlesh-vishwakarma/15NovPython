import React, { useState, useRef } from 'react';

function FeedbackFormRef() {
  const [name, setName] = useState('');
  const [message, setMessage] = useState('');
  const [submittedFeedback, setSubmittedFeedback] = useState(null);
  const messageTextareaRef = useRef(null);

  const focusMessage = () => {
    if (messageTextareaRef.current) {
      messageTextareaRef.current.focus();
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!name.trim() || !message.trim()) {
      alert('Please fill out both your name and feedback message.');
      return;
    }

    setSubmittedFeedback({ name, message });
    setName('');
    setMessage('');
  };

  return (
    <div className="component-card">
      <div className="card-top-action">
        <h3>4. Feedback Form (Programmatic Message Focus)</h3>
        <button
          type="button"
          className="btn btn-secondary"
          onClick={focusMessage}
        >
          ✏️ Focus Message Field
        </button>
      </div>

      <form onSubmit={handleSubmit} className="form-stack">
        <div className="form-group">
          <label htmlFor="fb-name">Your Name:</label>
          <input
            id="fb-name"
            type="text"
            className="form-control"
            placeholder="e.g. Mithlesh"
            value={name}
            onChange={(e) => setName(e.target.value)}
          />
        </div>

        <div className="form-group">
          <label htmlFor="fb-message">Feedback Message:</label>
          <textarea
            ref={messageTextareaRef}
            id="fb-message"
            className="form-control"
            rows="3"
            placeholder="Share your thoughts on the React assignment..."
            value={message}
            onChange={(e) => setMessage(e.target.value)}
          />
        </div>

        <button type="submit" className="btn btn-primary">
          Submit Feedback
        </button>
      </form>

      {submittedFeedback && (
        <div className="feedback-result">
          <h5>Latest Feedback Received:</h5>
          <p><strong>From:</strong> {submittedFeedback.name}</p>
          <p><strong>Message:</strong> "{submittedFeedback.message}"</p>
        </div>
      )}
    </div>
  );
}

export default FeedbackFormRef;

