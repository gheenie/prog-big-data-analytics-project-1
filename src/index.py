import os
from pathlib import Path

from task_2 import extract_urls
from task_3 import serial_download, parallel_download


if __name__ == '__main__':
    urls = extract_urls()

    output_folder = "data"
    output_folder_2 = "video_output"
    output_path = os.path.join(output_folder, output_folder_2)
    Path(output_path).mkdir(parents=True, exist_ok=True)

    serial_download(urls)
    parallel_download(urls)
