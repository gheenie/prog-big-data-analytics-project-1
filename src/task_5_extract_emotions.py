import json
import os
from concurrent.futures import ProcessPoolExecutor

from nrclex import NRCLex


def extract_emotions(text_file):
    input_folder = "data"
    input_folder_2 = "transcribed_text"
    input_path = os.path.join(input_folder, input_folder_2, text_file)

    text = ''
    with open(input_path, 'r') as file:
        text = file.read()
        
    emotion = NRCLex(text)

    output_folder = "data"
    output_folder_2 = "extracted_emotions"
    output_path = os.path.join(output_folder, output_folder_2, text_file)

    with open(output_path, 'w') as file:
        file.write(json.dumps(emotion.affect_frequencies))
    print(f'Extracted emotions has been written to {output_path}')


def parallel_extract_emotions(text_files):
    with ProcessPoolExecutor() as executor:
        executor.map(extract_emotions, text_files)
