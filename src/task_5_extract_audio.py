import os
from concurrent.futures import ProcessPoolExecutor

import moviepy.editor as mp


def extract_audio(video_file):
    input_folder = "data"
    input_folder_2 = "video_output"
    input_path = os.path.join(input_folder, input_folder_2, video_file)

    video = mp.VideoFileClip(input_path)

    output_folder = "data"
    output_folder_2 = "extracted_audio"
    output_path = os.path.join(output_folder, output_folder_2, video_file[:-4])
    output_path = f'{output_path}.wav'

    video.audio.write_audiofile(output_path)


def parallel_extract(video_files):
    with ProcessPoolExecutor() as executor:
        executor.map(extract_audio, video_files)
