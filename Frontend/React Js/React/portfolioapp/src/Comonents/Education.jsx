import React from 'react'

function Education() {
  return (
    <div className='p-20 bg-gray-200 flex justify-center flex-col gap-10'>
         <h2 className='text-3xl font-bolder text-center'>My Education </h2> 
        <table className="border-collapse border border-gray-400 ...">
  <thead>
    <tr>
      <th className="border border-gray-300 px-5 py-3">Srno</th>
       <th className="border border-gray-300 px-5 py-3">Degree</th>
        <th className="border border-gray-300 px-5 py-3">College/school</th>
         <th className="border border-gray-300 px-5 py-3">Year</th>
        <th className="border border-gray-300 px-5 py-3">Percentage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td className="border border-gray-300 px-5 py-3">1</td>
      <td className="border border-gray-300 px-5 py-3">B.Tech</td>
      <td className="border border-gray-300 px-5 py-3">Parul Institute</td>
      <td className="border border-gray-300 px-5 py-3">2016</td>
      <td className="border border-gray-300 px-5 py-3">76</td>
    </tr>
    <tr>
      <td className="border border-gray-300 px-5 py-3">1</td>
      <td className="border border-gray-300 px-5 py-3">B.Tech</td>
      <td className="border border-gray-300 px-5 py-3">Parul Institute</td>
      <td className="border border-gray-300 px-5 py-3">2016</td>
      <td className="border border-gray-300 px-5 py-3">76</td>
    </tr>
    <tr>
     <td className="border border-gray-300 px-5 py-3">1</td>
      <td className="border border-gray-300 px-5 py-3">B.Tech</td>
      <td className="border border-gray-300 px-5 py-3">Parul Institute</td>
      <td className="border border-gray-300 px-5 py-3">2016</td>
      <td className="border border-gray-300 px-5 py-3">76</td>
    </tr>
  </tbody>
</table>
    </div>
  )
}

export default Education