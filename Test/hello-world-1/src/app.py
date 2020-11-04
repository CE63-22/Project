import os

from flask import Flask, render_template

# pylint: disable=C0103
app = Flask(__name__)


@app.route('/')
def hello():
    """Return a simple HTML page with a friendly message."""
    message = "It's running!"

    return render_template('index.html', message=message)

from google.cloud import speech_v1 as speech

def speech_to_text(config, audio):
    client = speech.SpeechClient()
    response = client.recognize(config=config, audio=audio)
    print_sentences(response)

def print_sentences(response):
    for result in response.results:
        best_alternative = result.alternatives[0]
        transcript = best_alternative.transcript
        confidence = best_alternative.confidence
        print('-' * 80)
        print(f'Transcript: {transcript}')
        print(f'Confidence: {confidence:.0%}')
        
config = {'language_code': 'en-US'}
audio = {'uri': 'gs://cloud-samples-data/speech/brooklyn_bridge.flac'}

if __name__ == '__main__':
    speech_to_text(config, audio)
    '''server_port = os.environ.get('PORT', '8080')
    app.run(debug=False, port=server_port, host='0.0.0.0')'''
