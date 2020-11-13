import os
import io
import json

from flask import Flask, render_template
from pydub import AudioSegment

# pylint: disable=C0103
app = Flask(__name__)

sampleRate = 16000

with open('src/data.json') as json_file:
    data = json.load(json_file)
    datalist = data["data"]

index = 2

filejson = datalist[index]
lang = filejson["lang"]
        

def transcribe_file(filejson):
    from google.cloud import speech

    script = filejson["script"]
    path = filejson["path"]

    client = speech.SpeechClient()

    with io.open(path, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=sampleRate,
        language_code=lang,
    )

    operation = client.long_running_recognize(
        request={"config": config, "audio": audio}
    )
    operation = client.long_running_recognize(config=config, audio=audio)

    print("Waiting for operation to complete...")
    response = operation.result(timeout=90)

    for result in response.results:
        transcript = result.alternatives[0].transcript
        confidence = result.alternatives[0].confidence*100
        print(u"Transcript: {}".format(transcript))
        print("Confidence: {}%".format(confidence))
        print("Script: {}".format(script))
        if script.upper()==transcript.upper():
            print("Transcription Result: Matched")
        else:
            print("Transcription Result: Not matched")

def transcribe_gcs(filejson):
    from google.cloud import speech

    script = filejson["script"]
    path = filejson["path"]

    client = speech.SpeechClient()

    audio = speech.RecognitionAudio(uri=path)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.FLAC,
        sample_rate_hertz=sampleRate,
        language_code=lang,
    )

    response = client.recognize(config=config, audio=audio)

    for result in response.results:
        transcript = result.alternatives[0].transcript
        print("Transcript: "+transcript)
        print("Script: "+script)

        if script.upper()==transcript.upper():
            print("Transcription Result: Matched")
        else:
            print("Transcription Result: Not matched")

if __name__ == '__main__':
    print("\n\n---start---\n")
    if filejson["isURI"]:
        print("Transcribing File '"+filejson['name']+"' on URI: "+filejson['path'])
        transcribe_gcs(filejson)
    else:
        print("Transcribing File '"+filejson['name']+"' on path: "+filejson['path'])
        transcribe_file(filejson)
    print("\n----end----\n\n")

