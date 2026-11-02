import React, { useState } from 'react';

function LikeButton() {
  const [likes, setLikes] = useState(0);

  return (
    <div className="card">
      <h3>1. Like Button Event Demo</h3>
      <button
        type="button"
        className="btn btn-like"
        onClick={() => setLikes((prev) => prev + 1)}
      >
        ❤️ Likes: <span className="counter-badge">{likes}</span>
      </button>
    </div>
  );
}

export default LikeButton;

