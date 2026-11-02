import React, { useState } from 'react';

function StarRating({ totalStars = 5 }) {
  const [rating, setRating] = useState(0);
  const [hoveredRating, setHoveredRating] = useState(0);

  return (
    <div className="exercise-card">
      <h3>4. 5-Star Rating Selector</h3>
      <div className="star-container" role="radiogroup" aria-label="Rating selector">
        {Array.from({ length: totalStars }, (_, index) => {
          const starValue = index + 1;
          const isFilled = starValue <= (hoveredRating || rating);

          return (
            <button
              key={starValue}
              type="button"
              className={`star-btn ${isFilled ? 'filled' : 'empty'}`}
              onClick={() => setRating(starValue)}
              onMouseEnter={() => setHoveredRating(starValue)}
              onMouseLeave={() => setHoveredRating(0)}
              aria-label={`${starValue} star`}
            >
              ★
            </button>
          );
        })}
      </div>
      <p className="rating-status">
        {rating > 0 ? `You selected: ${rating} out of ${totalStars} stars` : 'No rating selected yet'}
      </p>
    </div>
  );
}

export default StarRating;

