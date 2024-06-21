import os
from pathlib import Path

from task_2 import extract_urls
from task_3 import serial_download, parallel_download
from task_5_extract_audio import parallel_extract


if __name__ == '__main__':
    urls = extract_urls()

    output_folder = "data"
    output_folder_2 = "video_output"
    output_path = os.path.join(output_folder, output_folder_2)
    Path(output_path).mkdir(parents=True, exist_ok=True)

    # serial_download(urls)
    # parallel_download(urls)

    # Assume directory contents are all files.
    video_files = [f for f in os.listdir(output_path)]
    print(video_files)

    output_folder = "data"
    output_folder_2 = "extracted_audio"
    output_path = os.path.join(output_folder, output_folder_2)
    Path(output_path).mkdir(parents=True, exist_ok=True)

    parallel_extract(video_files)
