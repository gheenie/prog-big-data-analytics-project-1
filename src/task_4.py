import os
import threading


file_lock = threading.Lock()


def log_downloaded_video(url, title):
    output_folder = "data"
    output_filename = "download_log.txt"
    output_path = os.path.join(output_folder, output_filename)

    file_lock.acquire()
    try:
        with open(output_path, 'a') as file:
            file.write(f'"URL": {url}, "Title": {title}\n')
        print(f"Log completed: {title}")
    finally:
        file_lock.release()
