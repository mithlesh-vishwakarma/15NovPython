import React from 'react'

function Home({username}) {
  return (
    <div>
        <h2>Home Page {username} </h2>
    </div>
  )
}

export function Test(){
      return(
         <>
            <h3>Test File</h3>
            <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Omnis animi hic, commodi odit illum nostrum ut ad ipsa beatae nam voluptate veniam consectetur culpa odio provident? Doloremque ut necessitatibus tempore.</p>
         </>
      )
}

export default Home