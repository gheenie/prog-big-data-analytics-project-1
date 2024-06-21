import os


def extract_urls(input_path):
    with open(input_path, 'r') as file:
        urls = file.readlines()

    for i, url in enumerate(urls):
        urls[i] = url.strip()
        
    print(urls)

    return urls
