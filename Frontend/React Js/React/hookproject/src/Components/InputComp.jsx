import React, { useState } from 'react'
import "./inputcomp.css"

function InputComp() {
    const [name,setName]=useState("");
    const [msg,setMsg]=useState("");

    const handleChange = (e)=>{
        setName(e.target.value)
 
    }
    const handleClick = ()=>{
        setMsg(`Welcome to react app:${name}`)
    }
  return (
    <div>
        <h2>User Info</h2>
        <fieldset className='fieldclass'>
            <legend>User Profile</legend>
            <label htmlFor="">Enter Username</label>
            <input type="text" name="username" id="" onChange={handleChange} />
            <button onClick={handleClick}>Submit</button>
            <p><b>{msg}</b></p>
        </fieldset>
    </div>
  )
}

export default InputComp