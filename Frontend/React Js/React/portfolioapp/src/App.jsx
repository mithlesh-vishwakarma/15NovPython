import { useState } from 'react'
import heroImg from './assets/hero.png'
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'
import Navbar from './Comonents/Navbar'
import Hero from './Comonents/Hero'
import Skill from './Comonents/Skill'
import Projects from './Comonents/Projects'
import Education from './Comonents/Education'


function App() {
  const [count, setCount] = useState(0)

  return (
    <>
       <Navbar/>
       <Hero/>
       <Skill/>
       <Projects/>
       <Education/>
    </>
  )
}

export default App
