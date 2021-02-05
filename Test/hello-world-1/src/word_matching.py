import os
import io
import json
import requests

from flask import Flask, render_template
from pydub import AudioSegment

# pylint: disable=C0103
app = Flask(__name__)
        

def transcribe_file(filejson):
    from google.cloud import speech

    script = filejson["script"]
    path = filejson["path"]
    sampleRate = filejson["sampleRate"]
    channel = filejson["channel_count"]
    lang = filejson["lang"]

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
        print("-" * 20)
        print("First alternative of result {}".format(i))
        print(u"Transcript: {}".format(transcript))
        print("Script: {}".format(script))
        for(int i=0;i<script.):
            for match in transcript.upper():
                if word==
        if script.upper()==transcript.upper():
            print("Transcription Result: Matched")
            print("-" * 20)
            return 1
        else:
            print("Transcription Result: Not matched")
        print(u"Channel Tag: {}".format(result.channel_tag))
    return 0

def transcribe_gcs(filejson):
    from google.cloud import speech

    script = filejson["script"]
    path = filejson["path"]
    channel = filejson["channel_count"]
    sampleRate = filejson["sampleRate"]
    lang = filejson["lang"]

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

        print("-" * 20)
        print("First alternative of result {}".format(i))
        print(u"Transcript: {}".format(transcript))
        print("Script: "+script)
        if script.upper()==transcript.upper():
            print("Transcription Result: Matched")
            print("-" * 20)
            return 1
        else:
            print("Transcription Result: Not matched")
        print(u"Channel Tag: {}".format(result.channel_tag))
    return 0

def wordMatcher_demo(index):

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

