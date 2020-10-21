'''def google_transcribe(audio_file_name):
    
    file_name = filepath + audio_file_name
    mp3_to_wav(file_name)

    # The name of the audio file to transcribe
    
    frame_rate, channels = frame_rate_channel(file_name)
    
    if channels > 1:
        stereo_to_mono(file_name)
    
    bucket_name = bucketname
    source_file_name = filepath + audio_file_name
    destination_blob_name = audio_file_name
    
    upload_blob(bucket_name, source_file_name, destination_blob_name)
    
    gcs_uri = 'gs://' + bucketname + '/' + audio_file_name
    transcript = ''
    
    client = speech.SpeechClient()
    audio = types.RecognitionAudio(uri=gcs_uri)

    config = types.RecognitionConfig(
    encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=frame_rate,
    language_code='en-US')

    # Detects speech in the audio file
    operation = client.long_running_recognize(config, audio)
    response = operation.result(timeout=10000)

    for result in response.results:
        transcript += result.alternatives[0].transcript
    
    delete_blob(bucket_name, destination_blob_name)
    return transcript

def write_transcripts(transcript_filename,transcript):
    f= open(output_filepath + transcript_filename,"w+")
    f.write(transcript)
    f.close()'''



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

speech_to_text(config, audio)
