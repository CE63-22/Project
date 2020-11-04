import os
import io

from flask import Flask, render_template
from pydub import AudioSegment

# pylint: disable=C0103
app = Flask(__name__)

lang = "en-US"
#lang = "th-TH"

#path = "gs://cloud-samples-tests/speech/brooklyn.flac"
#path = "C:\\Users\\Ithur\\Documents\\GitHub\\Project22\\Dataset\\08ith.mp3"
#path = "C:\\Users\\Ithur\\Documents\\GitHub\\Project22\\Test\\hello-world-1\\resource\\audio.raw"
#path = "C:\\Users\\Ithur\\Documents\\GitHub\\Project22\\Test\\hello-world-1\\resource\\audio2.raw"
path = "C:\\Users\\Ithur\\Documents\\GitHub\\Project22\\Test\\hello-world-1\\resource\\Recording (2).m4a"

def convert(source):
    if(source.endswith(".m4a")):
        print("\n\n---m4a---\n\n")
        source_m4a = AudioSegment.from_file(source, "m4a")
    song.export("source.raw", format="raw")

def transcribe_file(speech_file):
    from google.cloud import speech

    client = speech.SpeechClient()

    with io.open(speech_file, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code=lang,
    )

    operation = client.long_running_recognize(
        request={"config": config, "audio": audio}
    )
    operation = client.long_running_recognize(config=config, audio=audio)

    print("Waiting for operation to complete...")
    response = operation.result(timeout=90)

    for result in response.results:
        print(u"Transcript: {}".format(result.alternatives[0].transcript))
        print("Confidence: {}".format(result.alternatives[0].confidence))

def transcribe_gcs(gcs_uri):
    from google.cloud import speech

    client = speech.SpeechClient()

    audio = speech.RecognitionAudio(uri=gcs_uri)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.FLAC,
        sample_rate_hertz=16000,
        language_code=lang,
    )

    response = client.recognize(config=config, audio=audio)

    for result in response.results:
        print(u"Transcript: {}".format(result.alternatives[0].transcript))


if __name__ == '__main__':
    '''if path.startswith("gs://"):
        transcribe_gcs(path)
    else:
        transcribe_file(path)'''
    convert(path)
    print("\n\n---end---\n\n")

