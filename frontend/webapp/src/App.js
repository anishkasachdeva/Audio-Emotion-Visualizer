import logo from './logo.svg';
import './App.css';
import React from 'react';
import CartesianPlane from './Component/CartesianPlane';

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

// export default App;


import Plot from 'react-plotly.js'

/**
 * Create array num length with random values from 0 to mul
 */
function randArr(num, mul) {
  const arr = [];
  const index = [];
  for (let i = 0; i < num; i++) {
    arr.push(Math.random() * mul)
    index.push(i);
  }
  return arr;
}

/**
 * Main application component
 */
// function App() {
//   return (
//     <div>
//     for(var i=0; i<5; i++)
//     {
//     <Plot
//       data={[
//         {
//           // x: randArr(20, 3), 
//           // y: randArr(20, 3), 
//           // z: randArr(20, 3),
//           x: [1,2,3,4,5], 
//           y: [5,6,7,8,9], 
//           z: [10,12,13,14,15], 
//           mode: 'markers', 
//           type:'scatter3d',
//         }
//       ]}
//       layout={{
//         height: 800,
//         width: 1200,
//         title: `3D Views`,
//       }}
//       onRelayout={(figure) => console.log(figure)}
//     />
//     }
//     </div>
//   );
// }

// export default function App() {
//   const runCallback = (cb) => {
//     return cb();
//   };

//   return (
//     <div>
//       {
//         runCallback(() => {
//           const row = [];
//           for (var i = 0; i < 5; i++) {
//             row.push(<p key={i}>{i}</p>);
//           }
//           return row;
//         })
//       }
//     </div>
//   );
// }

// export default App;
export default function App() {
  var rows = [], i = 0, len = 1;
  while (++i <= len) rows.push(i);

  return (
    <tbody>
      {rows.map(function (i) {
        return <CartesianPlane key={i} index={i} />;
      })}
    </tbody>
  );
}
