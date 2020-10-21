'''

if __name__ == "__main__":
    for audio_file_name in os.listdir(filepath):
        transcript = google_transcribe(audio_file_name)
        transcript_filename = audio_file_name.split('.')[0] + '.txt'
        write_transcripts(transcript_filename,transcript)'''

import quickstart

from google.cloud import speech_v1 as speech


def speech_to_text(config, audio):
    client = speech.SpeechClient()
    response = client.recognize(config, audio)
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


if __name__ == "__main__":
    #quickstart.run()
    speech_to_text(config, audio)

    
