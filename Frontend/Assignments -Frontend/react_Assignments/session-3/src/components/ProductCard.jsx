import React from 'react';
import PropTypes from 'prop-types';

function ProductCard({ productName, price }) {
  return (
    <article className="product-card">
      <div className="product-badge">Top Deal</div>
      <h3 className="product-title">{productName}</h3>
      <p className="product-price">₹{price.toLocaleString('en-IN')}</p>
      <button type="button" className="product-btn">Add to Cart</button>
    </article>
  );
}

ProductCard.propTypes = {
  productName: PropTypes.string.isRequired,
  price: PropTypes.number.isRequired,
};

export default ProductCard;

