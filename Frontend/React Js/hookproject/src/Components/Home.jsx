import React, { useEffect, useState } from 'react'

function Home() {
  const [qty, setQty] = useState(0);
  const [counter, setCounter] = useState(0);
  const [msg, setMsg] = useState(null)
  // useEffect(()=>{
  //     console.log("use effect called run on every render");

  // })
  // useEffect(() => {
  //   console.log("run useEffect on mount");

  // }, [])
  useEffect(() => {


    console.log("use effect called when qty change");

    return () => {
      setTimeout(() => {
        setMsg(null)
      }, 2000)
    }

  }, [msg])
  return (
    <div>
      {
        msg && <p style={{ color: 'green' }}>
          {msg}
        </p>
      }
      <div>
        <button onClick={() => {
          setMsg("Data Created");
        }}>
          Submit
        </button>
      </div>
      <input type="number" name="" id="" value={qty} onChange={(e) => {
        setQty(e.target.value)
      }} />
      <div>
        <button onClick={() => {
          setCounter(counter + 1)
        }}>+</button><span>{counter}</span>
      </div>
    </div>
  )
}

export default Home