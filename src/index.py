import os
from pathlib import Path

from task_2 import extract_urls
from task_3 import serial_download, parallel_download
from task_5_extract_audio import parallel_extract
from task_5_transcribe_audio import parallel_transcribe


if __name__ == '__main__':
    urls = extract_urls()

    output_folder = "data"
    output_folder_2 = "video_output"
    output_path = os.path.join(output_folder, output_folder_2)
    Path(output_path).mkdir(parents=True, exist_ok=True)

    # serial_download(urls)
    # parallel_download(urls)

    # Extract file paths of the videos.
    video_files = [f for f in os.listdir(output_path)]
    print(video_files)

    output_folder = "data"
    output_folder_2 = "extracted_audio"
    output_path = os.path.join(output_folder, output_folder_2)
    Path(output_path).mkdir(parents=True, exist_ok=True)

    # parallel_extract(video_files)

    audio_files = [f for f in os.listdir(output_path)]
    print(audio_files)

    output_folder = "data"
    output_folder_2 = "transcribed_text"
    output_path = os.path.join(output_folder, output_folder_2)
    Path(output_path).mkdir(parents=True, exist_ok=True)

    parallel_transcribe(audio_files)
