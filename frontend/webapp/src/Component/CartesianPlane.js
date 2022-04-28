import Plot from 'react-plotly.js';
import React from 'react';

class CartesianPlane extends React.Component {
    render() {
      return(
        <Plot
              data={[
                {
                  // x: randArr(20, 3), 
                  // y: randArr(20, 3), 
                  // z: randArr(20, 3),
                  x: [1,2,3,4,5], 
                  y: [5,6,7,8,9], 
                  z: [10,12,13,14,15], 
                  mode: 'markers', 
                  type:'scatter3d',
                }
              ]}
              layout={{
                height: 800,
                width: 1200,
                title: `3D Views`,
              }}
              onRelayout={(figure) => console.log(figure)}
            />
      )
    }
  }

export default CartesianPlane; 