// import React, { useState, useEffect } from 'react'
// import { useParams } from 'react-router-dom'

// function ParkDetails() {
//     const { stateName } = useParams();
//     const [parkData, setParkData] = useState(null);

//     useEffect(()=>{
//         fetch(`/parks/${stateName}`)
//         .then(res => res.json())
//         .then(data => setParkData(data))
//     }, [stateName])

//     if (!parkData){
//         return <div>Loading...</div>
//     }

//   return (
//     <div>
//         <h1>{parkData.name}</h1>
//         <h2>Activities</h2>
//         <ul>
//             {parkData.activities.map((activity, index) => (
//                 <li key={index}> {activity}</li>
//             ))}
//         </ul>

//     </div>
//   )
// }

// export default ParkDetails