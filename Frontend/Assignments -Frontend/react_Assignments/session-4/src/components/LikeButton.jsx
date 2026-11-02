import React, { useState } from 'react';

function LikeButton() {
  const [likes, setLikes] = useState(0);

  const handleLike = () => {
    setLikes((prev) => prev + 1);
  };

  return (
    <div className="exercise-card">
      <h3>1. Like Button</h3>
      <button
        type="button"
        className="like-btn"
        onClick={handleLike}
        aria-label="Like post"
      >
        ❤️ Likes: <span className="badge-count">{likes}</span>
      </button>
    </div>
  );
}

export default LikeButton;

