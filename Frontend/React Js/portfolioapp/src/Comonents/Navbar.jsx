import React from 'react'

function Navbar() {
  return (
    <div className='bg-gray-900 text-white px-20 py-5 md:px-10'>
       <div className="md:flex justify-between items-center">
            <div className="logodiv">
                <span className='text-3xl font-bolder'>MDevlops</span>

            </div>
            <div className="navitems md:flex gap-10">
                <div>Navitem-1</div>
                <div>Navitem-2</div>
                <div>Navitem-3</div>
                <div>Navitem-4</div>
                <div>Navitem-5</div>
            </div>
       </div>
    </div>
  )
}

export default Navbar