import React from 'react'

function Skill() {
  return (
    <div className='p-10'>
        <h2 className='text-3xl font-bolder text-center'>My Skill</h2>

        <div className=" grid grid-cols-6 gap-4 px-10 py-10 rounded">
                <div className="flex justify-center items-center w-20 h-20 rounded-full bg-orange-200 hover:bg-gray-900 hover:text-orange-200 hover:zoom-125">
                  <abbr title="Html Hypertext markrup language"> <i class="fa-brands fa-html5" style={{fontSize:'2em'}}></i></abbr>
                </div>
                 <div className="flex justify-center items-center w-20 h-20 rounded-full bg-blue-200">
                   <i class="fa-brands fa-css3-alt" style={{fontSize:'2em'}}></i>
                </div>
                 <div className="flex justify-center items-center w-20 h-20 rounded-full bg-yellow-200">
                   <i class="fa-brands fa-js" style={{fontSize:'2em'}}></i>
                </div>
                 <div className="flex justify-center items-center w-20 h-20 rounded-full bg-green-200">
                   <i class="fa-brands fa-node" style={{fontSize:'2em'}}></i>
                </div>
                 <div className="flex justify-center items-center w-20 h-20 rounded-full bg-blue-200">
                   <i class="fa-brands fa-react" style={{fontSize:'2em'}}></i>
                </div>
                 <div className="flex justify-center items-center w-20 h-20 rounded-full bg-green-300">
                   <i class="fa-brands fa-mdb" style={{fontSize:'2em'}}></i>
                </div>
                 <div className="flex justify-center items-center w-20 h-20 rounded-full bg-blue-300">
                   <i class="fa-brands fa-python" style={{fontSize:'2em'}}></i>
                </div>
                <div className="flex justify-center items-center w-20 h-20 rounded-full bg-orange-200">
                   <i class="fa-brands fa-postgresql" style={{fontSize:'2em'}}></i>
                </div><div className="flex justify-center items-center w-20 h-20 rounded-full bg-orange-200">
                   <i class="fa-brands fa-database" style={{fontSize:'2em'}}></i>
                </div>
                <div className="flex justify-center items-center w-20 h-20 rounded-full bg-orange-200">
                   <i class="fa-brands fa-flutter" style={{fontSize:'2em'}}></i>
                </div>
                <div className="flex justify-center items-center w-20 h-20 rounded-full bg-orange-200">
                   <i class="fa-brands fa-openai" style={{fontSize:'2em'}}></i>
                </div>
                <div className="flex justify-center items-center w-20 h-20 rounded-full bg-orange-200">
                   <i class="fa-brands fa-copilot" style={{fontSize:'2em'}}></i>
                </div>
              
        </div>
    </div>
  )
}

export default Skill