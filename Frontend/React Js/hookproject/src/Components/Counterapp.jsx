import React, { useState } from 'react'

function Counterapp() {
    const [count,setCount]=useState(100)

    const incre = ()=>{
        setCount(count+1)
    }
    const decre = ()=>{
        setCount(count-1)
    }
  return (
    <div>
        <h1 style={{color:"blue"}}>Counter App</h1>
        <button onClick={incre}>+</button>
        <span>{count}</span>
        <button onClick={decre}>-</button>
    </div>
  )
}

export default Counterapp