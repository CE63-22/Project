import os
import argparse

from pydub import AudioSegment
# AudioSegment.converter = r"C:\\Users\\Ithur\\anaconda3\\pkgs\\imageio-2.9.0-py_0\\site-packages\\imageio\\plugins\\ffmpeg.exe"

formats_to_convert = ['.m4a']

def wavConverter(filename):
    print("\n\n------------conversion start------------\n")
    print('PREPARING TO CONVERT: ' + str(filename))
    if filename.endswith(tuple(formats_to_convert)):
        # directory = "C:/Users/Ithur/Documents/GitHub/Project22/Test/hello-world-1/resources/"
        directory = "resources/"

        c = "ffmpeg -i "+filename+" "+filename.replace('m4a', 'wav')
        os.system(c)

        # filepath =directory + filename
        # print('\tfilepath = ' + str(filepath))

        # (path, file_extension) = os.path.splitext(filepath)
        # print('\tpath = ' + str(path))
        # print('\tfile_extension = ' + str(file_extension))

        # track = AudioSegment.from_file(filepath,'m4a')
        # wav_filename = filename.replace('m4a', 'wav')
        # wav_path = directory + wav_filename
        # print('CONVERTING: ' + str(filepath))
        # file_handle = track.export(wav_path, format='wav')

        # (path, file_extension) = os.path.splitext(filepath)
        # file_extension_final = file_extension.replace('.', '')
        # try:
        #     track = AudioSegment.from_file(filepath,'m4a')
        #     wav_filename = filename.replace('m4a', 'wav')
        #     wav_path = 'resource/' + wav_filename
        #     print('CONVERTING: ' + str(filepath))
        #     file_handle = track.export(wav_path, format='wav')
        #     os.remove(filepath)
        # except:
        #     print("ERROR CONVERTING " + str(filepath))
        print("\n------------conversion end------------\n")
    return 1