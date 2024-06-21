import os
from concurrent.futures import ProcessPoolExecutor

import speech_recognition as sr


def transcribe_audio(audio_file):
    input_folder = "data"
    input_folder_2 = "extracted_audio"
    input_path = os.path.join(input_folder, input_folder_2, audio_file)
    
    print(f'Transcribing audio: {input_path}')
    recognizer = sr.Recognizer()
    with sr.AudioFile(input_path) as source:
        audio = recognizer.record(source)
    text = recognizer.recognize_google(audio)
    print(f'Transcribe finished: {input_path}')

    output_folder = "data"
    output_folder_2 = "transcribed_text"
    output_path = os.path.join(output_folder, output_folder_2, audio_file)[:-4]
    output_path = f'{output_path}.txt'

    with open(output_path, 'w') as file:
            file.write(text)
    print(f'Text has been written to {output_path}')


def parallel_transcribe(audio_files):
    with ProcessPoolExecutor() as executor:
        executor.map(transcribe_audio, audio_files)
