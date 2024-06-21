import os


def extract_urls():
    output_folder = "data"
    output_filename = "video_urls.txt"
    output_path = os.path.join(output_folder, output_filename)

    with open(output_path, 'r') as file:
        urls = file.readlines()

    for i, url in enumerate(urls):
        urls[i] = url.strip()
        
    print(urls)

    return urls
