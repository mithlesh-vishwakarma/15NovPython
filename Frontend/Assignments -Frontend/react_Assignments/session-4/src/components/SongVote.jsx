import React, { useState } from 'react';

function SongVote({ songTitle = 'Calm Down - Rema & Selena Gomez' }) {
  const [votes, setVotes] = useState(0);

  const upvote = () => {
    setVotes((prev) => prev + 1);
  };

  const downvote = () => {
    setVotes((prev) => (prev > 0 ? prev - 1 : 0));
  };

  return (
    <div className="exercise-card">
      <h3>3. Song Upvote / Downvote</h3>
      <p className="song-title">🎵 {songTitle}</p>
      <div className="vote-controls">
        <button
          type="button"
          className="vote-btn upvote"
          onClick={upvote}
          aria-label="Upvote song"
        >
          ▲ Upvote
        </button>
        <span className="votes-count">{votes} votes</span>
        <button
          type="button"
          className="vote-btn downvote"
          onClick={downvote}
          disabled={votes === 0}
          aria-label="Downvote song"
        >
          ▼ Downvote
        </button>
      </div>
    </div>
  );
}

export default SongVote;

