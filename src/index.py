from pathlib import Path
from task_2 import extract_urls
from task_3 import serial_download, parallel_download


if __name__ == '__main__':
    urls = extract_urls()

    Path('data/video_output').mkdir(parents=True, exist_ok=True)
    serial_download(urls)
    parallel_download(urls)
