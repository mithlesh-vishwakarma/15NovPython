import React from 'react'
import "styled-components"
import styled from 'styled-components'

function Profile() {
    const MyHead = styled.h1`
        font-size:3em;
        color:blue;
        text-decoration:underline;
    `;
  return (
    <div >
        <MyHead>John Abraham</MyHead>
        <h2>Full Stack Developer</h2>
        <p>A Full Stack Developer is a software developer who works on both the frontend and backend of a web application, including database management and API integration.</p>
    </div>
  )
}

export default Profile