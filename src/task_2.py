import os


def extract_urls():
    input_folder = "data"
    input_filename = "video_urls.txt"
    input_path = os.path.join(input_folder, input_filename)

    with open(input_path, 'r') as file:
        urls = file.readlines()

    for i, url in enumerate(urls):
        urls[i] = url.strip()
        
    print(urls)

    return urls
