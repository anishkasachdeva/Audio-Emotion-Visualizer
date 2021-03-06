# -*- coding: utf-8 -*-
"""tempFeatureExtraction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15UTd6EAXakboiN8Kt-QuTdC0YEoF1rBE
"""

import librosa
import numpy as np
import pandas as pd
from os import listdir
from os.path import isfile, join
import warnings
import sklearn
import matplotlib.pyplot as plt
import antropy
from sklearn.cross_decomposition import PLSRegression
from sklearn.preprocessing import scale 
from sklearn.model_selection import RepeatedKFold
from sklearn import model_selection
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_squared_error, r2_score
from sklearn import datasets, linear_model, metrics
from sklearn.decomposition import PCA
import pickle
from scipy.stats import yeojohnson
import matplotlib.animation as animation
import matplotlib
matplotlib.use('TkAgg')
from mpl_toolkits.mplot3d import Axes3D
from playsound import playsound

'''
    function: extract_features
    input: path to mp3 files
    output: csv file containing features extracted
    
    This function reads the content in a directory and for each mp3 file detected
    reads the file and extracts relevant features using librosa library for audio
    signal processing
'''

def run_model(feature_set, model='pls', apply_transformation=True, toPredict=['valence', 'energy', 'tension']):
  feature_set.dropna(how = 'any', axis = 0) 
  audio_df = pd.read_csv('features_combined.csv')
  # audio_df.drop(['Unnamed: 0'], axis = 1, inplace = True)
  audio_df = audio_df.dropna(how = 'any',axis = 0)
  X = audio_df.loc[:, "tempo" : "frame_var"]
  featureName = list(X)
  if apply_transformation == True:
    for name in featureName:
      X[name], lam = yeojohnson(X[name])
      feature_set[name] = yeojohnson(feature_set[name], lmbda=lam)
  X = pd.DataFrame(X)
  emotionRatingPrediction = {}
  r2s = {}
  for pre in toPredict:
    y = audio_df[pre]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)
    if model == "pls":
      pls = PLSRegression(n_components = 10)
      pls.fit(X_train, y_train)
      # rmse = np.sqrt(mean_squared_error(y_test, pls.predict(X_test)))
      r2 = pls.score(X_train, y_train)
      pred = pls.predict(feature_set)
    elif model == "lr" or model == "lr_pca":
      reg = linear_model.LinearRegression()
      reg.fit(X_train, y_train)
      r2 = reg.score(X_train, y_train)
      pred = reg.predict(feature_set)
    elif model == "lr_pca":
      pca = PCA(n_components = 11)
      X_train_transformed = pca.fit_transform(X_train)
      feature_set_transformed = pca.transform(feature_set)
      explained_variance = pca.explained_variance_ratio_
      reg = linear_model.LinearRegression()
      reg.fit(X_train_transformed, y_train)
      r2 = reg.score(X_train_transformed, y_train)
      pred = reg.predict(feature_set_transformed)
    emotionRatingPrediction[pre] = pred.flatten()
    r2s[pre] = r2
  return emotionRatingPrediction, r2s


def extract_feature(audio):
    feature_set = pd.DataFrame()  # Feature Matrix
    
    # Individual Feature Vectors
    songname_vector = []
    tempo_vector = []
    total_beats = []
    average_beats = []
    chroma_stft_mean = []
    chroma_stft_std = []
    chroma_stft_var = []
    chroma_cq_mean = []
    chroma_cq_std = []
    chroma_cq_var = []
    chroma_cens_mean = []
    chroma_cens_std = []
    chroma_cens_var = []
    mel_mean = []
    mel_std = []
    mel_var = []
    mfcc_mean = []
    mfcc_std = []
    mfcc_var = []
    mfcc_delta_mean = []
    mfcc_delta_std = []
    mfcc_delta_var = []
    rms_mean = []
    rms_std = []
    rms_var = []
    cent_mean = []
    cent_std = []
    cent_var = []
    spec_bw_mean = []
    spec_bw_std = []
    spec_bw_var = []
    contrast_mean = []
    contrast_std = []
    contrast_var = []
    rolloff_mean = []
    rolloff_std = []
    rolloff_var = []
    entropy_fft = []
    entropy_welch = []
    novelty_mean = []
    novelty_std = []
    novelty_var = []
    poly_mean = []
    poly_std = []
    poly_var = []
    tonnetz_mean = []
    tonnetz_std = []
    tonnetz_var = []
    zcr_mean = []
    zcr_std = []
    zcr_var = []
    harm_mean = []
    harm_std = []
    harm_var = []
    perc_mean = []
    perc_std = []
    perc_var = []
    frame_mean = []
    frame_std = []
    frame_var = []
    
    y, sr = librosa.load(audio)
    S = np.abs(librosa.stft(y))
    
    time = 0
    while time < len(y) - sr * 15:
      curr = y[time:min(len(y), time + 15 * sr)]
      time += sr * 15 

      # Extracting Features
      tempo, beats = librosa.beat.beat_track(y = curr, sr = sr, hop_length = int(sr * 0.046 * 0.5))
      chroma_stft = librosa.feature.chroma_stft(y = curr, sr = sr, n_fft = int(sr * 0.046), hop_length = int(sr * 0.046 * 0.5))
      chroma_cq = librosa.feature.chroma_cqt(y = curr, sr = sr)
      chroma_cens = librosa.feature.chroma_cens(y = curr, sr = sr)
      melspectrogram = librosa.feature.melspectrogram(y = curr, sr = sr, n_fft = int(sr * 0.046), hop_length = int(sr * 0.046 * 0.5))
      rms = librosa.feature.rms(y = curr, frame_length = int(sr * 0.046),  hop_length = int(sr * 0.046 * 0.5))
      cent = librosa.feature.spectral_centroid(y = curr, sr = sr, n_fft = int(sr * 0.046), hop_length = int(sr * 0.046 * 0.5))
      spec_bw = librosa.feature.spectral_bandwidth(y = curr, sr = sr, win_length = int(sr * 0.046), hop_length = int(sr * 0.046 * 0.5))
      contrast = librosa.feature.spectral_contrast(S = S, sr = sr, n_fft = int(sr * 0.046), hop_length = int(sr * 0.046 * 0.5))
      rolloff = librosa.feature.spectral_rolloff(y = curr, sr = sr, n_fft = int(sr * 0.046))
      entropy_fft_val = antropy.spectral_entropy(curr, sf = sr)
      entropy_welch_val = antropy.spectral_entropy(curr, sf = sr, method = 'welch')
      novelty = librosa.onset.onset_strength(y = curr, sr = sr, n_fft = int(sr * 0.046), hop_length = int(sr * 0.046 * 0.5))
      poly_features = librosa.feature.poly_features(S = S, sr = sr, n_fft = int(sr * 0.046), hop_length = int(sr * 0.046 * 0.5))
      tonnetz = librosa.feature.tonnetz(y = curr, sr = sr)
      zcr = librosa.feature.zero_crossing_rate(y = curr, frame_length = int(sr * 0.046), hop_length = int(sr * 0.046 * 0.5))
      harmonic = librosa.effects.harmonic(curr)
      percussive = librosa.effects.percussive(curr)
      
      mfcc = librosa.feature.mfcc(y = curr, sr = sr)
      mfcc_delta = librosa.feature.delta(mfcc, width=max(3, min(9, (mfcc.shape[-1] // 2) * 2 - 1)))

      onset_frames = librosa.onset.onset_detect(y = curr, sr = sr, hop_length = int(sr * 0.046 * 0.5))
      frames_to_time = librosa.frames_to_time(onset_frames[:20], sr = sr)
      

      # Transforming Features
      songname_vector.append(audio)  # song name
      tempo_vector.append(tempo) # tempo
      total_beats.append(sum(beats))  # beats
      average_beats.append(np.average(beats))
      chroma_stft_mean.append(np.mean(chroma_stft))  # chroma stft
      chroma_stft_std.append(np.std(chroma_stft))
      chroma_stft_var.append(np.var(chroma_stft))
      chroma_cq_mean.append(np.mean(chroma_cq)) # chroma cq
      chroma_cq_std.append(np.std(chroma_cq))
      chroma_cq_var.append(np.var(chroma_cq))
      chroma_cens_mean.append(np.mean(chroma_cens))  # chroma cens
      chroma_cens_std.append(np.std(chroma_cens))
      chroma_cens_var.append(np.var(chroma_cens))
      mel_mean.append(np.mean(melspectrogram))  # melspectrogram
      mel_std.append(np.std(melspectrogram))
      mel_var.append(np.var(melspectrogram))
      mfcc_mean.append(np.mean(mfcc))  # mfcc
      mfcc_std.append(np.std(mfcc))
      mfcc_var.append(np.var(mfcc))
      mfcc_delta_mean.append(np.mean(mfcc_delta))  # mfcc delta
      mfcc_delta_std.append(np.std(mfcc_delta))
      mfcc_delta_var.append(np.var(mfcc_delta))
      rms_mean.append(np.mean(rms))  # rms
      rms_std.append(np.std(rms))
      rms_var.append(np.var(rms))
      cent_mean.append(np.mean(cent))  # cent
      cent_std.append(np.std(cent))
      cent_var.append(np.var(cent))
      spec_bw_mean.append(np.mean(spec_bw))  # spectral bandwidth
      spec_bw_std.append(np.std(spec_bw))
      spec_bw_var.append(np.var(spec_bw))
      contrast_mean.append(np.mean(contrast))  # contrast
      contrast_std.append(np.std(contrast))
      contrast_var.append(np.var(contrast))
      rolloff_mean.append(np.mean(rolloff))  # rolloff
      rolloff_std.append(np.std(rolloff))
      rolloff_var.append(np.var(rolloff))
      entropy_fft.append(entropy_fft_val)  # rolloff
      entropy_welch.append(entropy_welch_val)
      novelty_mean.append(np.mean(novelty))  # rolloff
      novelty_std.append(np.std(novelty))
      novelty_var.append(np.var(novelty))
      poly_mean.append(np.mean(poly_features))  # poly features
      poly_std.append(np.std(poly_features))
      poly_var.append(np.var(poly_features))
      tonnetz_mean.append(np.mean(tonnetz))  # tonnetz
      tonnetz_std.append(np.std(tonnetz))
      tonnetz_var.append(np.var(tonnetz))
      zcr_mean.append(np.mean(zcr))  # zero crossing rate
      zcr_std.append(np.std(zcr))
      zcr_var.append(np.var(zcr))
      harm_mean.append(np.mean(harmonic))  # harmonic
      harm_std.append(np.std(harmonic))
      harm_var.append(np.var(harmonic))
      perc_mean.append(np.mean(percussive))  # percussive
      perc_std.append(np.std(percussive))
      perc_var.append(np.var(percussive))
      frame_mean.append(np.mean(frames_to_time))  # frames
      frame_std.append(np.std(frames_to_time))
      frame_var.append(np.var(frames_to_time))
      

    # Concatenating Features into one csv and json format
    feature_set['tempo'] = tempo_vector  # tempo 
    feature_set['total_beats'] = total_beats  # beats
    feature_set['average_beats'] = average_beats
    feature_set['chroma_stft_mean'] = chroma_stft_mean  # chroma stft
    feature_set['chroma_stft_std'] = chroma_stft_std
    feature_set['chroma_stft_var'] = chroma_stft_var
    feature_set['chroma_cq_mean'] = chroma_cq_mean  # chroma cq
    feature_set['chroma_cq_std'] = chroma_cq_std
    feature_set['chroma_cq_var'] = chroma_cq_var
    feature_set['chroma_cens_mean'] = chroma_cens_mean  # chroma cens
    feature_set['chroma_cens_std'] = chroma_cens_std
    feature_set['chroma_cens_var'] = chroma_cens_var
    feature_set['melspectrogram_mean'] = mel_mean  # melspectrogram
    feature_set['melspectrogram_std'] = mel_std
    feature_set['melspectrogram_var'] = mel_var
    feature_set['mfcc_mean'] = mfcc_mean  # mfcc
    feature_set['mfcc_std'] = mfcc_std
    feature_set['mfcc_var'] = mfcc_var
    feature_set['mfcc_delta_mean'] = mfcc_delta_mean  # mfcc delta
    feature_set['mfcc_delta_std'] = mfcc_delta_std
    feature_set['mfcc_delta_var'] = mfcc_delta_var
    feature_set['rms_mean'] = rms_mean  # rms
    feature_set['rms_std'] = rms_std
    feature_set['rms_var'] = rms_var
    feature_set['cent_mean'] = cent_mean  # cent
    feature_set['cent_std'] = cent_std
    feature_set['cent_var'] = cent_var
    feature_set['spec_bw_mean'] = spec_bw_mean  # spectral bandwidth
    feature_set['spec_bw_std'] = spec_bw_std
    feature_set['spec_bw_var'] = spec_bw_var
    feature_set['contrast_mean'] = contrast_mean  # contrast
    feature_set['contrast_std'] = contrast_std
    feature_set['contrast_var'] = contrast_var
    feature_set['rolloff_mean'] = rolloff_mean  # rolloff
    feature_set['rolloff_std'] = rolloff_std
    feature_set['rolloff_var'] = rolloff_var
    feature_set['entropy_fft'] = entropy_fft
    feature_set['entropy_welch'] = entropy_welch
    feature_set['novelty_mean'] = novelty_mean  # rolloff
    feature_set['novelty_std'] = novelty_std
    feature_set['novelty_var'] = novelty_var
    feature_set['poly_mean'] = poly_mean  # poly features
    feature_set['poly_std'] = poly_std
    feature_set['poly_var'] = poly_var
    feature_set['tonnetz_mean'] = tonnetz_mean  # tonnetz
    feature_set['tonnetz_std'] = tonnetz_std
    feature_set['tonnetz_var'] = tonnetz_var
    feature_set['zcr_mean'] = zcr_mean  # zero crossing rate
    feature_set['zcr_std'] = zcr_std
    feature_set['zcr_var'] = zcr_var
    feature_set['harm_mean'] = harm_mean  # harmonic
    feature_set['harm_std'] = harm_std
    feature_set['harm_var'] = harm_var
    feature_set['perc_mean'] = perc_mean  # percussive
    feature_set['perc_std'] = perc_std
    feature_set['perc_var'] = perc_var
    feature_set['frame_mean'] = frame_mean  # frames
    feature_set['frame_std'] = frame_std
    feature_set['frame_var'] = frame_var

    emotionRatingPrediction = run_model(feature_set)
    return emotionRatingPrediction

def func(num, dataSet, line):
    # NOTE: there is no .set_data() for 3 dim data...
    line.set_data(dataSet[0:2, :num])    
    line.set_3d_properties(dataSet[2, :num])    
    return line


def main():
    print('Choose a number from 1-2 for the corresponding audio to be played')
    audio = input()
    audio = './Soundtrack_Snippets/' + audio + '.mp3'
    emotionRatingPrediction,r2s = extract_feature(audio)
    print(emotionRatingPrediction)
    x = np.round_(emotionRatingPrediction['valence'],2)
    y = np.round_(emotionRatingPrediction['energy'],2)
    t = np.round_(emotionRatingPrediction['tension'],2)


    dataSet = np.array([x, y, t])
    numDataPoints = len(t)
    print(dataSet)
    # GET SOME MATPLOTLIB OBJECTS
    fig = plt.figure()
    ax = Axes3D(fig)
    
    # NOTE: Can't pass empty arrays into 3d version of plot()
    line = plt.plot(dataSet[0], dataSet[1], dataSet[2], lw=2, c = 'g', marker='o')[0] # For line plot
    ax.set_xlabel('Valence')
    ax.set_ylabel('Energy')
    ax.set_zlabel('Tension')
    ax.set_title('Emotion Trajectory of ' + audio + '.mp3')
    
    # Creating the Animation object
    line_ani = animation.FuncAnimation(fig, func, frames=numDataPoints, fargs=(dataSet,line), interval = 15000, blit=False)
    
    playsound(audio, False)
    plt.show()


if __name__ == "__main__":
  main()