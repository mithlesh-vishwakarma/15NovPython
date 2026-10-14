import { useState } from 'react'
import './App.css'
import Counterapp from './Components/Counterapp'
import InputComp from './Components/InputComp'
import Profile from './Components/Profile'
import Home from './Components/Home'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <Counterapp/>
      <InputComp/>
      <Home/>
     
    </>
  )
}

export default App
