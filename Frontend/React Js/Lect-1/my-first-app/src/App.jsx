import { useState } from 'react'
import heroImg from './assets/hero.png'
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'
import './App.css'
import About from './components/about.jsx'
import Home from './components/home.jsx'
import Card from './components/card.jsx'
import products from './components/product.js'

function App() {
  const [count, setCount] = useState(0)
  console.log(products);

  return (
    <>
      <h1>hii this is my first app</h1>
      {/* <About />
      <Home /> */}
      {
        products && products.map((product, index) => (
          <Card
            key={index}
            title={product.title}
            description={product.description}
            price={product.price}
            category={product.category}
            image={product.image}
          />
        ))
      }
      {/* <Card /> */}
    </>
  )
}

export default App
