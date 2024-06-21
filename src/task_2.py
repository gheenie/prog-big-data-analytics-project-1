def extract_urls(file_path):
    with open(file_path, 'r') as file:
        urls = file.readlines()

        return urls
