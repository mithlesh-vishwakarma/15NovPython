import { useState } from 'react'
import hero from './assets/hero.png'
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'
import './App.css'
import Home from './Components/Home'
import About from './Components/About'
import { Test } from './Components/Home'
import Card from './Components/Card'
import {products} from './Components/Products'

function App() {
 
  const username="Megha Patel"
  console.log(products);
  
  return (
    <div  style={{
      display: "flex",
      justifyContent: "center",
      flexWrap: "wrap"
    }}>
        {/* <h1>Welcome to app:{username}</h1>
        <img src={hero} alt="" height={'100px'} width={'100px'} />
        <Home username={username}/>
        <About/>

        <Test/> */}
        {
          products && products.map((index)=>(
            <Card singleProduct={index}/>
          ))
        }
        
    </div>
  )
}

export default App
