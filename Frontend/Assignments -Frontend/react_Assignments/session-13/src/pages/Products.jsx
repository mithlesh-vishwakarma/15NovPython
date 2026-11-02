import React from 'react';

function Products() {
  const products = [
    { id: 1, name: 'Cloud Hosting Bundle', price: '₹999/mo', tag: 'Popular' },
    { id: 2, name: 'Custom Domain & SSL', price: '₹499/yr', tag: 'Essential' },
    { id: 3, name: 'CDN Global Edge Network', price: '₹1499/mo', tag: 'Fast' },
  ];

  return (
    <div className="page-box">
      <h1>DeployPro Products & Services</h1>
      <p className="lead-text">Scalable frontend tooling and deployment services.</p>

      <div className="products-grid">
        {products.map((p) => (
          <div key={p.id} className="product-item-card">
            <span className="prod-tag">{p.tag}</span>
            <h3>{p.name}</h3>
            <p className="prod-price">{p.price}</p>
            <button type="button" className="action-btn">Get Started</button>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Products;

