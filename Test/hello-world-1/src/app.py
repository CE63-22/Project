import os
import io

from flask import Flask, render_template
from pydub import AudioSegment

# pylint: disable=C0103
app = Flask(__name__)

sampleRate = 16000

lang_list = ["en-US","th-TH"]
lang = lang_list[0]

path_list=[
    "gs://cloud-samples-tests/speech/brooklyn.flac",    #0
    "C:\\Users\\Ithur\\Documents\\GitHub\\Project22\\Dataset\\08ith.mp3",   #1
    "resource\\audio.raw", #2
    "resource\\audio2.raw",    #3
    "resource\\Recording (2).m4a",  #4
    "resource\\Recording (2).wav",  #5
    "resource\\commercial_mono.wav" #6
]
path = path_list[6]

def convert(source):
    if(source.endswith(".m4a")):
        print(" --------m4a--------\n")
        audio = AudioSegment.from_file(source, "m4a")
        audio.export("raw/source.raw", format="raw")
        print(" -finised conversion-\n")
        return "raw/source.raw"
    elif(source.endswith(".wav")):
        print(" --------wav--------\n")
        audio = AudioSegment.from_file(source, "wav")
        audio.export("raw/source.raw", format="raw")
        print(" -finised conversion-\n")
        return "raw/source.raw"
    else:
        return source
        

def transcribe_file(speech_file):
    from google.cloud import speech

    client = speech.SpeechClient()

    with io.open(speech_file, "rb") as audio_file:
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
        print(u"Transcript: {}".format(result.alternatives[0].transcript))
        print("Confidence: {}".format(result.alternatives[0].confidence))

def transcribe_gcs(gcs_uri):
    from google.cloud import speech

    client = speech.SpeechClient()

    audio = speech.RecognitionAudio(uri=gcs_uri)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.FLAC,
        sample_rate_hertz=sampleRate,
        language_code=lang,
    )

    response = client.recognize(config=config, audio=audio)

    for result in response.results:
        print(u"Transcript: {}".format(result.alternatives[0].transcript))


if __name__ == '__main__':
    print("\n\n---start---\n")
    if path.startswith("gs://"):
        transcribe_gcs(path)
    else:
        path = convert(path)
        print("Transcribe File on path: "+path)
        transcribe_file(path)
    print("\n----end----\n\n")

