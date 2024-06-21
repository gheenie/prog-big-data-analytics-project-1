from pathlib import Path
from task_2 import extract_urls


if __name__ == '__main__':
    urls = extract_urls('data/task_2/video_urls.txt')
    print(urls)

    Path('data/task_3').mkdir(parents=True, exist_ok=True)
