import os
from concurrent.futures import ProcessPoolExecutor

from translate import Translator


def translate_text(text_file):
    input_folder = "data"
    input_folder_2 = "transcribed_text"
    input_path = os.path.join(input_folder, input_folder_2, text_file)

    text = ''
    with open(input_path, 'r') as file:
        text = file.read()
        
    translator = Translator(from_lang='en', to_lang='es')
    # Only translate first 500 characters.
    translation = translator.translate(text[:500])

    output_folder = "data"
    output_folder_2 = "translated_text"
    output_path = os.path.join(output_folder, output_folder_2, text_file)

    with open(output_path, 'w') as file:
        file.write(translation)
    print(f'Translation has been written to {output_path}')


def parallel_translate(text_files):
    with ProcessPoolExecutor() as executor:
        executor.map(translate_text, text_files)
