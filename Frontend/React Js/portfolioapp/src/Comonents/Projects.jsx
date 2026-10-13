import React, { useMemo } from 'react'
import { projects } from './ProjectsArray';
import './project.css'

function Projects() {
    const category = ['All','Web','React','Python'];

   
    
  return (
    <div className='p-20' >
         <h2 className='text-3xl font-bolder text-center'>My Projects</h2> 
         <div className="flex  p-5 justify-center gap-5">
            {
                category.map((index)=>(
                    <span className='bg-blue-300 px-5 py-2 rounded-full text-white'>{index}</span>
                ))
            }
         </div>
         <div className="grid grid-cols-3 p-10 gap-10">
            {
                projects.map((index)=>(
                    <div className="col w-100% h-50  rounded ">
                         <img src={index.image} alt={index.title}  />
                        <div className="overlay ">
                            <h3 className="text-white">{index.title}</h3>
                            </div>
                       
                    </div>
                ))
            }
                
                
        </div> 
    </div>
  )
}

export default Projects