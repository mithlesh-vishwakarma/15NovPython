import React from 'react'

function Card({singleProduct}) {
  
    
    const cardStyle = {
    width: "300px",
    border: "1px solid #ddd",
    borderRadius: "10px",
    overflow: "hidden",
    boxShadow: "0 4px 8px rgba(0,0,0,0.2)",
    fontFamily: "Arial",
    margin: "20px",
    backgroundColor: "white"
  };

  const imgStyle = {
    width: "100%",
    height: "200px",
    objectFit: "cover"
  };

  const contentStyle = {
    padding: "15px"
  };

  const btnStyle = {
    backgroundColor: "#007bff",
    color: "white",
    padding: "10px 20px",
    border: "none",
    borderRadius: "5px",
    cursor: "pointer"
  };
  return (
    <div style={cardStyle}>
      <img
        src={singleProduct.pimage}
        alt="Watch"
        style={imgStyle}
      />

      <div style={contentStyle}>
        <h2 style={{ margin: "0 0 10px" }}>{singleProduct.name}</h2>

        <p style={{ color: "#666", lineHeight: "1.5" }}>
          {singleProduct.description}
        </p>

        <h3 style={{ color: "green" }}>₹2,499</h3>

        <button style={btnStyle}>
          Buy Now
        </button>
      </div>
    </div>
  )
}

export default Card