import React from 'react'
import person from '../assets/person.jpeg'

function Hero() {
    return (
        <div className='bg-gray-100 px-15 py-20 max-md:px-5 max-md:py-10'>
            <div className="md:grid grid-cols-2">
                <div className="max-md:order-last">
                          <h1 className='text-5xl text-gray-900 font-bolder pb-5 max-sm:text-2xl max-sm:text-center lg:order-2'>Megha Patel</h1>
                    <p>A <b>Full Stack Developer</b> is a software developer who works on both the frontend and backend of a web application. They can build the user interface, develop server-side logic, manage databases, create APIs, and connect all parts of an application together.</p>
                    <button>Contact me</button>
                </div>
                
                <div className="hero-img  max-md:order-first basis-50%">
                    <img src={person} alt="" className='w-50 h-50 rounded-full mx-auto' />
                </div>
            </div>
        </div>
    )
}

export default Hero