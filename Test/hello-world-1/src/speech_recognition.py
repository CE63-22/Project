import scipy
from scipy.io import wavfile
from scipy import signal
import numpy as np
import matplotlib.pyplot as plt

import librosa
import librosa.display

import os
import glob

def analyzeAudio(audioName):
    audioPath = "./resources/"+audioName
    print("Analyzing audio : "+audioName)
    print("On path : "+audioPath)
    samplerate, data = wavfile.read(audioPath)
    length = data.shape[0] / samplerate
    print(samplerate)
    print(data)
    print(type(data))

    c = 0
    bits = np.empty((0, 2), int)
    bitsize = int(samplerate/10)
    print(length)
    while c<length*10:
        bitdata = 0
        c_remain = length*10-c
        if(c_remain<1):
            last_calculation_index = data.shape[0]
        else:
            last_calculation_index = bitsize*(c+1)

        # Debug Printing
        # print('loop: '+str(c))
        # print('\tloop start bit: '+str(bitsize*c))
        # print('\tloop last bit: '+str(last_calculation_index))
        # print('\tloop remaining: '+str(c_remain))
        
        for i in range(bitsize*c,last_calculation_index):
            bitdata += data[i]
        # print('\tbitdata = '+str(bitdata))
        avgbitdata = bitdata/bitsize
        # print('\tavgbitdata = '+str(avgbitdata))
        bits = np.append(bits, np.array([avgbitdata]), axis=0)
        c+=1
    print(bits)
    print(type(bits))

    samplerate, data = wavfile.read(audioPath)
    print(f"number of channels = {data.shape[1]}")
    length = data.shape[0] / samplerate
    # length = data.shape[0] / 100
    print(f"length = {length}s")

    time0 = np.linspace(0., length, data.shape[0])
    time1 = np.linspace(0., length, int(length*10)+1)
    plt.plot(time0, data[:, 0], label="Left channel")
    plt.plot(time0, data[:, 1], label="Right channel")
    plt.plot(time1, bits[:, 0], label="Average")
    plt.legend()
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")
    plt.show()

def speedAnalizer(speed):
    result = 1
    isFaster = False
    if(speed>160):
        diff = speed-160
        result=(1000-diff)/1000
        isFaster = True
    if(speed<150):
        diff = 150-speed
        result=(diff-100)/100
    # speed(150-160) ok
    # speed maximum 1000?
    # speed from 160-1160 : diff from 0-1000: result from 1-0
    # speed from 50-150 : diff from 100-0: result from 0-1
    return [result,isFaster]