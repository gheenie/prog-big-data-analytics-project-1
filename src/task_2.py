def extract_urls(file_path):
    with open(file_path, 'r') as file:
        urls = file.readlines()

        return urls


if __name__ == '__main__':
    urls = extract_urls('data/video_urls.txt')
    print(urls)
