import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
from playsound import playsound
from tempfeatureextraction import *
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

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
 
 

def animate(emotionRatingPrediction):


# THE DATA POINTS
# t = np.arange(0,20,0.2) # This would be the z-axis ('t' means time here)
# x = np.cos(t)-1
# y = 1/2*(np.cos(2*t)-1)
# print('Choose a number from 1-5 for the corresponding audio to be played')
# audio = input()
# audio = './Soundtrack_Snippets/' + audio + '.mp3'

# emotionRatingPrediction = extract_feature(audio)
# print(emotionRatingPrediction)
# playsound(audio, False)
    print(type(emotionRatingPrediction))
    print(emotionRatingPrediction)
    print(emotionRatingPrediction[0])
    x = np.round_(emotionRatingPrediction[0],2)
    y = np.round_(emotionRatingPrediction[1],2)
    t = np.round_(emotionRatingPrediction[2],2)

    
    print(x)
    print(y)
    print(t)

    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    # ax = Axes3D(fig)
    
    # t = np.arange(0,20,0.2)
    # x = np.cos(t)-1
    # y = 1/2*(np.cos(2*t)-1)

    # print(type(t))
    
    
    # For scatter plot
    # ax.scatter(x, y, t, c='r', marker='o')
    ax.plot(2, 3, 4, c='r', marker='o')
    # ax.plot(x, y, t, c='r', marker='o')
    # # For line plot
    # ax.plot(x, y, t, c='g')
    
    ax.set_xlabel('X(t)')
    ax.set_ylabel('Y(t)')
    ax.set_zlabel('time')
    ax.set_title('Trajectory of electron for E vector along [120]')

    # Creating the Animation object
    # line_ani = animation.FuncAnimation(fig, func, frames=numDataPoints, fargs=(dataSet,line), interval=500, blit=False)
    #line_ani.save(r'AnimationNew.mp4')


    plt.show()

# def main():
    # print('Choose a number from 1-5 for the corresponding audio to be played')
    # audio = input()
    # audio = './Soundtrack_Snippets/' + audio + '.mp3'
    # emotionRatingPrediction = extract_feature(audio)
    # print(emotionRatingPrediction)
    # # playsound(audio, False)
    # run(np.array(emotionRatingPrediction['valence']),np.array(emotionRatingPrediction['energy']),np.array(emotionRatingPrediction['tension']))

# if __name__ == "__main__":
#     main()