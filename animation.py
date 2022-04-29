import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
from playsound import playsound
  
# playsound('/path/note.wav')
 

# def selectAudio(audio):



# References
# https://gist.github.com/neale/e32b1f16a43bfdc0608f45a504df5a84
# https://towardsdatascience.com/animations-with-matplotlib-d96375c5442c
# https://riptutorial.com/matplotlib/example/23558/basic-animation-with-funcanimation
 
# ANIMATION FUNCTION
def func(num, dataSet, line):
    # NOTE: there is no .set_data() for 3 dim data...
    line.set_data(dataSet[0:2, :num])    
    line.set_3d_properties(dataSet[2, :num])    
    return line
 
 
# THE DATA POINTS
# t = np.arange(0,20,0.2) # This would be the z-axis ('t' means time here)
# x = np.cos(t)-1
# y = 1/2*(np.cos(2*t)-1)

def run():
    x = np.array([1,2,3,4,5,6,7,8,9,10])
    y = np.array([10,22,34,46,51,64,77,85,92,10])
    t = np.array([15,26,32,48,52,61,79,86,93,100])
    print(x)
    print(y)
    print(t)
    dataSet = np.array([x, y, t])
    numDataPoints = len(t)
    
    # GET SOME MATPLOTLIB OBJECTS
    fig = plt.figure()
    ax = Axes3D(fig)
    
    # NOTE: Can't pass empty arrays into 3d version of plot()
    line = plt.plot(dataSet[0], dataSet[1], dataSet[2], lw=2, c='g')[0] # For line plot
    
    # AXES PROPERTIES]
    # ax.set_xlim3d([limit0, limit1])
    ax.set_xlabel('X(t)')
    ax.set_ylabel('Y(t)')
    ax.set_zlabel('time')
    ax.set_title('Trajectory of electron for E vector along [120]')
    
    # Creating the Animation object
    line_ani = animation.FuncAnimation(fig, func, frames=numDataPoints, fargs=(dataSet,line), interval=500, blit=False)
    #line_ani.save(r'AnimationNew.mp4')
    
    
    plt.show()

def main():
    print('Choose a number from 1-5 for the corresponding audio to be played')
    audio = input()
    audio = './Soundtrack_Snippets/' + audio + '.mp3'
    valence = extractFeature(audio)
    energy = extractFeature(audio)
    tension = extractFeature(audio)
    playsound(audio, False)
    run()

if __name__ == "__main__":
    main()