from concurrent.futures import ThreadPoolExecutor
import threading
import time

from task_4 import log_downloaded_video

from pytube import YouTube


def download_video(url):
    yt = YouTube(url)
    stream = yt.streams.get_highest_resolution()
    print(f"Downloading video: {yt.title}")
    stream.download(output_path='data/video_output')
    print(f"Download completed: {yt.title}")
    log_downloaded_video(url, yt.title)


def serial_download(urls):
    start = time.perf_counter()
    for url in urls:
        download_video(url)
    end = time.perf_counter()
    print(f'Serial download finished in {end - start} seconds')


semaphore = threading.Semaphore(5)


def download_video_with_semaphores(url):
    semaphore.acquire()
    download_video(url)
    semaphore.release()


def parallel_download(urls):
    start = time.perf_counter()
    with ThreadPoolExecutor() as executor:
        executor.map(download_video_with_semaphores, urls)
    end = time.perf_counter()
    print(f'Parallel download finished in {end - start} seconds')
