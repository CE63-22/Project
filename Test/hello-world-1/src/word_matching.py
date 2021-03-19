import os
import io
import json
import requests
import deepcut
from m4atowav import wavConverter
from scipy.io import wavfile

from flask import Flask, render_template
from pydub import AudioSegment

# pylint: disable=C0103
app = Flask(__name__)

wordCount = 0
lenght = 0
        
def transcribe_file(filepath,scriptpath):
    from google.cloud import speech

    global wordCount
    global lenght

    sampleRate, data = wavfile.read(filepath)

    script = open(scriptpath,encoding='utf-8').read()
    path = filepath
    # sampleRate = 48000
    channel = data.shape[1]
    lang = "th-TH"

    script_words=deepcut.tokenize(script)
    script_words=spaceEliminator(script_words)

    print("-"*10+"PLEASE WAIT"+"-"*10)

    client = speech.SpeechClient()

    with io.open(path, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=sampleRate,
        language_code=lang,
        audio_channel_count=channel,
        enable_separate_recognition_per_channel=True,
    )

    response = client.recognize(config=config, audio=audio)

    for i,result in enumerate(response.results):
        alternative = result.alternatives[0]
        transcript = alternative.transcript

        transcript_words=deepcut.tokenize(transcript)
        transcript_words=spaceEliminator(transcript_words)
        wordCount = len(transcript_words)
        lenght = data.shape[0] / sampleRate

        print("-" * 20)
        print("First alternative of result {}".format(i))
        print(u"Transcript: {}".format(transcript))
        print("Script: {}".format(script))
        #print("Deepcut: {}".format(deepcut.tokenize(transcript)))
        match = 0
            
            #choosing which listhas the lesser lenght...
        if len(script_words) < len(transcript_words):
            shorterScriptCount = len(script_words)
        else:
            shorterScriptCount = len(transcript_words)

            # ...and use it in matching.
        for i in range(shorterScriptCount):
            # print("\tDEBUG: MATCHING WORD:( "+transcript_words[i]+" , "+script_words[i]+" )") # DEBUG
            if script_words[i] == transcript_words[i]:
                # print("\tDEBUG: MATCHING RESULT: MATCHED")        # DEBUG
                match+=1
            # else:
                # print("\tDEBUG: MATCHING RESULT: NOT MATCHED")    # DEBUG
        match_result=match/len(script_words)
        print("Matched Result: {} %".format(match_result*100))      # show match result in percentage.
        print(u"Channel Tag: {}".format(result.channel_tag))        
    return match_result

def transcribe_file_fromJson(filejson):
    from google.cloud import speech

    # script = filejson["script"]
    script = open(filejson["script_path"],encoding='utf-8').read()
    # while(wavConverter(filejson["name"])!=1):
    #     print("converting...")
    path = filejson["path"]
    # path = 'resource/' + filejson["name"].replace('m4a','wav')
    sampleRate = filejson["sampleRate"]
    channel = filejson["channel_count"]
    lang = filejson["lang"]

    script_words=deepcut.tokenize(script)
    script_words=spaceEliminator(script_words)

    print("-"*10+"PLEASE WAIT"+"-"*10)

    client = speech.SpeechClient()

    with io.open(path, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=sampleRate,
        language_code=lang,
        audio_channel_count=channel,
        enable_separate_recognition_per_channel=True,
    )

    response = client.recognize(config=config, audio=audio)

    for i,result in enumerate(response.results):
        alternative = result.alternatives[0]
        transcript = alternative.transcript

        transcript_words=deepcut.tokenize(transcript)
        transcript_words=spaceEliminator(transcript_words)

        print("-" * 20)
        print("First alternative of result {}".format(i))
        print(u"Transcript: {}".format(transcript))
        print("Script: {}".format(script))
        #print("Deepcut: {}".format(deepcut.tokenize(transcript)))
        match = 0
            
            #choosing which listhas the lesser lenght...
        if len(script_words) < len(transcript_words):
            shorterScriptCount = len(script_words)
        else:
            shorterScriptCount = len(transcript_words)

            # ...and use it in matching.
        for i in range(shorterScriptCount):
            # print("\tDEBUG: MATCHING WORD:( "+transcript_words[i]+" , "+script_words[i]+" )") # DEBUG
            if script_words[i] == transcript_words[i]:
                # print("\tDEBUG: MATCHING RESULT: MATCHED")        # DEBUG
                match+=1
            # else:
                # print("\tDEBUG: MATCHING RESULT: NOT MATCHED")    # DEBUG
        match_result=match/len(script_words)
        print("Matched Result: {} %".format(match_result*100))      # show match result in percentage.
        print(u"Channel Tag: {}".format(result.channel_tag))        
    return match_result

def transcribe_gcs(filejson):
    from google.cloud import speech

    script = filejson["script"]
    path = filejson["path"]
    channel = filejson["channel_count"]
    sampleRate = filejson["sampleRate"]
    lang = filejson["lang"]

    script_words=deepcut.tokenize(script)
    script_words=spaceEliminator(script_words)

    client = speech.SpeechClient()

    audio = speech.RecognitionAudio(uri=path)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=sampleRate,
        language_code=lang,
        audio_channel_count=channel,
        enable_separate_recognition_per_channel=True,
    )

    response = client.recognize(config=config, audio=audio)

    for i,result in enumerate(response.results):
        alternative = result.alternatives[0]
        transcript = alternative.transcript

        transcript_words=deepcut.tokenize(transcript)
        transcript_words=spaceEliminator(transcript_words)

        print("-" * 20)
        print("First alternative of result {}".format(i))
        print(u"Transcript: {}".format(transcript))
        print("Script: "+script)
        match = 0
            
            #choosing which listhas the lesser lenght...
        if len(script_words) < len(transcript_words):
            shorterScriptCount = len(script_words)
        else:
            shorterScriptCount = len(transcript_words)

            # ...and use it in matching.
        for i in range(shorterScriptCount):
            if script_words[i] == transcript_words[i]:
                match+=1
        match_result=match/len(script_words)
        print("Matched Result: {} %".format(match_result*100))      # show match result in percentage.
        print(u"Channel Tag: {}".format(result.channel_tag))
    return match_result

def wordMatcher_demo_index(index):
    # index
        # 0 = gsSample in English from google (not being used in Demo)
        # 1 = wavSample in English from google
        # 2 = wavSample in English
        # 3 = wavSample in Thai
        # 4 = 04Noey.wav
        # 5 = 04Noey.m4a

    with open('src/data.json', encoding="utf-8") as json_file:
        data = json.load(json_file)
        datalist = data["data"]

    filejson = datalist[index]

    
    if filejson["isURI"]:
        print("Transcribing File '"+filejson['name']+"' on URI: "+filejson['path'])
        return transcribe_gcs(filejson)
    else:
        print("Transcribing File '"+filejson['name']+"' on path: "+filejson['path'])
        return transcribe_file(filejson)

def wordMatcher_demo(filename,scriptname):

    filepath = "resources/"+filename
    scriptpath = "resources/script/"+scriptname

    print("Transcribing File '"+filename+"' on path: "+filepath)
    return transcribe_file(filepath,scriptpath)
    # return 1

def speedCounter_f():
    # print(f'wordCount = {wordCount} words, lenght = {lenght} secounds')
    speed = wordCount/(lenght/60)
    return speed

def spaceEliminator(list):
    poppingIndexes = []
    for i in range(len(list)):
        if list[i] == " ":
            poppingIndexes.append(i)                                # adding index in the list that is space in to poppingIndexes list.
            # print("\tDEBUG: POP INDEX: "+str(i)+" "+list[i])      # DEBUG
    # print("\tDEBUG: POP LIST: {}".format(poppingIndexes))         # DEBUG
    for i in reversed(poppingIndexes):
        list.pop(i)                                                 # remove space from the list according to the index given by poppingIndexes in reverse. (why in reverse? so the greater number of index don't change while removing a list's element.)
        # print("\tDEBUG: POPING: "+str(i)+" "+list[i])             # DEBUG
    return list