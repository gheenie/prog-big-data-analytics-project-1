from pathlib import Path
from task_2 import extract_urls
from task_3 import serial_download


if __name__ == '__main__':
    urls = extract_urls('data/video_urls.txt')
    print(urls)

    Path('data/video_output').mkdir(parents=True, exist_ok=True)
    serial_download(urls)
