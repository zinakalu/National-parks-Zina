// import React, { useState } from 'react';
// import './ParkCard.css';

// function ParkCard({ singlePark, setParks, parks }) {
//   const { visits, park, id } = singlePark;

//   const [isVisited, setIsVisited] = useState(false);
//   const [visitCount, setVisitCount] = useState(visits);

//   function handleClick() {
//     setIsVisited(!isVisited);

//     if (!isVisited) {
//       setVisitCount(visitCount + 1);
//     } else {
//       setVisitCount(visitCount - 1);
//     }

//     const updatedParks = parks.map((park) => {
//       if (park.id === id) {
//         park.visits = visitCount;
//       }
//       return park;
//     });

//     setParks(updatedParks);
//   }

//   return (
//     <div className="card">
//       <p>{park}</p>
//       <p>
//         <span className="likes">❤️ {visitCount}</span>
//         <button onClick={handleClick}>
//           {isVisited ? 'Unlike' : 'Like'}
//         </button>
//       </p>
//     </div>
//   );
// }

// export default ParkCard;