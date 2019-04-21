'''
etude_ninja: for slicing etudes to make audio datasets

util/wav_file_util.py

Utilities for dealing with wav files, at this point just loading them, getting data with time points, and saving them again.

'''

import numpy as np
import math
import argparse
from scipy.io import wavfile

class Wav_file:

    def __init__(self, filePath):
        """
        Initialize a Wav_file, starting with a file to load using scipy
        :param filePath: str
            The full path of the audio file to open.
        """

        # load it up
        self.sRate, self.data = wavfile.read(filePath)

    def get_slice(self, start_time, end_time):
        """
        Return a slice of a file as raw data

        :param start_time: float
            The insert time in the Wav_file for the slice
        :param end_time: float
            The end of the requested slice in seconds
        :return: ndarray of audio sample values
        """

        start_index = math.floor(start_time*self.sRate)
        end_index = math.floor(end_time*self.sRate)
        return self.data[start_index:end_index:1]

    def save_slice(self, start_time, end_time, fileName):
        """
        Get a slice from the wav file using get_slice and save it to a file.

        :param start_time: float
            The insert time in the Wav_file for the slice
        :param end_time: float
            The end of the requested slice in seconds
        :param fileName: str
            The full path of the output file
        :return: Nothing, you get nothing
        """
        wavfile.write(fileName, self.sRate, self.get_slice(start_time, end_time))

    ''' 
    TODO: just play a damn slice
    '''

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("inputFileName", type=str,
                        help="wav file to use for input")
    parser.add_argument("outputFileName", type=str,
                        help="wav file to use for output")
    parser.add_argument('start_time', type=float,
                        help="Start of the audio in seconds")
    parser.add_argument('end_time', type=float,
                        help="End of the audio in seconds")
    args = parser.parse_args()
    filePath = args.inputFileName
    outFilePath = args.outputFileName
    start_time = args.start_time
    end_time = args.end_time

    # automate to put out a big bunch of notes from notespans file 
    inputFile = Wav_file(filePath)
    inputFile.save_slice(start_time, end_time, outFilePath)


if __name__ == '__main__':
    main()
