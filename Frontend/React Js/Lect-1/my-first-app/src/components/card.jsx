import React from 'react'

function card(product) {
    function Card({ title, description, price, image, category }) {
        const cardStyle = {
            width: "300px",
            overflow: "hidden",
            border: "1px solid #e5e7eb",
            borderRadius: "12px",
            backgroundColor: "#ffffff",
            boxShadow: "0 4px 12px rgba(0, 0, 0, 0.08)",
        };

        const imageStyle = {
            width: "100%",
            height: "200px",
            objectFit: "cover",
            display: "block",
        };

        const contentStyle = {
            padding: "20px",
        };

        const categoryStyle = {
            color: "#2563eb",
            fontSize: "14px",
            fontWeight: "600",
        };

        const titleStyle = {
            margin: "8px 0",
            fontSize: "22px",
            color: "#111827",
        };

        const descriptionStyle = {
            color: "#6b7280",
            lineHeight: "1.5",
        };

        const priceStyle = {
            fontSize: "22px",
            color: "#111827",
            margin: "15px 0",
        };

        const buttonStyle = {
            width: "100%",
            padding: "11px",
            border: "none",
            borderRadius: "8px",
            backgroundColor: "#2563eb",
            color: "white",
            fontSize: "15px",
            fontWeight: "600",
            cursor: "pointer",
        };
        return (
            <div style={cardStyle}>
                <img
                    src={product.image}
                    alt={product.title}
                    style={imageStyle}
                />

                <div style={contentStyle}>
                    <span style={categoryStyle}>{product.category}</span>

                    <h2 style={titleStyle}>{product.title}</h2>

                    <p style={descriptionStyle}>{product.description}</p>

                    <h3 style={priceStyle}>₹{product.price}</h3>

                    <button style={buttonStyle}>
                        Buy Now
                    </button>
                </div>
            </div>
        )
    }
}
export default card