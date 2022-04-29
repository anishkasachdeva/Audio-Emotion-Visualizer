import Plot from 'react-plotly.js';
import React from 'react';

class CartesianPlane extends React.Component {
  constructor(props) {
    super(props);
    this.state =
              { curr_x: 0,
                curr_y: 0,
                curr_z: 0,
                x: [1, 2, 3, 4, 5], 
                y: [5, 6, 7, 8, 9], 
                z: [10, 12, 13, 14, 15]
              };
  }

  delay(i) {
    setTimeout(() => {
          this.setState({ curr_x: this.state.x[i],
            curr_y: this.state.y[i],
            curr_z: this.state.z[i]
          });
        }, 5000);
  }

  componentDidMount() {
    for(let i = 0; i < 5; i++) {
      this.delay(i)
      // console.log(i)
      // setTimeout(() => {
      //   this.setState({ curr_x: this.state.x[i],
      //                   curr_y: this.state.y[i],
      //                   curr_z: this.state.z[i]
      //                 });
      // }, 10000);
    }
  }
  
//   render() {
//     return (
//       <div>
//         <p
//           style = {{
//             color: this.state.color,
//             backgroundColor: 'rgba(0,0,0,0.88)',
//             textAlign: 'center',
//             paddingTop: 20,
//             width: 400,
//             height: 80,
//             margin: 'auto'
//           }}
//         >
//           GeeksForGeeks
//         </p>
  
//       </div>
//     );
//   }
// }
    render() {
      return(
        <div>
          {this.state.curr_x}
          <br></br>
          {this.state.curr_y}
          <br></br>
          {this.state.curr_z}

        {/* <Plot
              data={[
                {
                  x: [this.state.curr_x], 
                  y: [this.state.curr_y], 
                  z: [this.state.curr_z], 
                  mode: 'markers', 
                  type:'scatter3d',
                  // markerTyoe : 'cross'
                }
              ]}
              layout = {{
                height: 800,
                width: 1200,
                title: `3D Views`,
              }}
              onRelayout={(figure) => console.log(figure)}
            /> */}
        </div>
      );
    }
  }

export default CartesianPlane; 