import { useState } from 'react'
import './App.css'
// import Counterapp from './Components/Counterapp'
// import InputComp from './Components/InputComp'
import Profile from './Components/Profile'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      {/* <Counterapp/>
      <InputComp/> */}
      <Profile/>
    </>
  )
}

export default App
