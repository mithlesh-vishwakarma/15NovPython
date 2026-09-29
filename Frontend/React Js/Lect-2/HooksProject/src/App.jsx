import { useState } from 'react'
import './App.css'

function App() {
  const [count, setCount] = useState(0)
  const [name, setName] = useState("")
  const [msg, setMsg] = useState("")

  function handleNameChange(event) {
    setName(event.target.value)
  }

  function handleClick() {
    setMsg(`Welcome to counter App ${name}`)
  }

  function increment() {
    setCount(count + 1)
  }

  function decrement() {
    setCount(count - 1)
  }

  function reset() {
    setCount(0)
  }

  return (
    <>
      <div className="container">
        <h1>Counter</h1>
        <p>{count}</p>
        <button onClick={increment}>Increment</button>
        <button onClick={decrement}>Decrement</button>
        <button onClick={reset}>Reset</button>

        <input type="text" value={name} onChange={handleNameChange} placeholder='Enter your name' />
        <p>{msg}</p>
        <button onClick={handleClick}>Greet Me</button>
      </div>
    </>
  )
}

export default App
