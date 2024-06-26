import asyncio
import os
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import time

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


def multiprocessing_extract(video_files):
    start = time.perf_counter()
    with ProcessPoolExecutor() as executor:
        executor.map(extract_audio, video_files)
    end = time.perf_counter()
    print(f'Multiprocessing audio extraction finished in {end - start} seconds')


def serial_extract(video_files):
    start = time.perf_counter()
    for video_file in video_files:
        extract_audio(video_file)
    end = time.perf_counter()
    print(f'Serial audio extraction finished in {end - start} seconds')


def threading_extract(video_files):
    start = time.perf_counter()
    with ThreadPoolExecutor() as executor:
        executor.map(extract_audio, video_files)
    end = time.perf_counter()
    print(f'Threading audio extraction finished in {end - start} seconds')


async def extract_audio_async(video_file):
    input_folder = "data"
    input_folder_2 = "video_output"
    input_path = os.path.join(input_folder, input_folder_2, video_file)

    video = mp.VideoFileClip(input_path)

    output_folder = "data"
    output_folder_2 = "extracted_audio"
    output_path = os.path.join(output_folder, output_folder_2, video_file[:-4])
    output_path = f'{output_path}.wav'

    video.audio.write_audiofile(output_path)


async def concurrent_extract(video_files):
    start = time.perf_counter()
    coroutines = [extract_audio_async(video_file) for video_file in video_files]
    await asyncio.gather(*coroutines)
    end = time.perf_counter()
    print(f'Concurrent audio extraction finished in {end - start} seconds')
