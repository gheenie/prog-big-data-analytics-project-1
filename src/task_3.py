import time

from pytube import YouTube


def download_video(url):
    yt = YouTube(url)
    stream = yt.streams.get_highest_resolution()
    print(f"Downloading video: {yt.title}")
    stream.download(output_path='data/video_output')
    print(f"Download completed: {yt.title}")


def serial_download(urls):
    start = time.perf_counter()
    for url in urls:
        download_video(url)
    end = time.perf_counter()
    print(f'Serial download finished in {end - start} seconds')
