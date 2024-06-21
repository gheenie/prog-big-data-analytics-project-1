import os
from concurrent.futures import ProcessPoolExecutor

from textblob import TextBlob


def analyse_sentiment(text_file):
    input_folder = "data"
    input_folder_2 = "transcribed_text"
    input_path = os.path.join(input_folder, input_folder_2, text_file)

    text = ''
    with open(input_path, 'r') as file:
        text = file.read()
        
    blob = TextBlob(text)
    print(blob.sentiment)

    output_folder = "data"
    output_folder_2 = "sentiment_analysis"
    output_path = os.path.join(output_folder, output_folder_2, text_file)

    with open(output_path, 'w') as file:
        file.write(f'Polarity: {blob.sentiment.polarity}, Subjectivity: {blob.sentiment.subjectivity}')
    print(f'Sentiment analysis has been written to {output_path}')


def parallel_sentiment(text_files):
    with ProcessPoolExecutor() as executor:
        executor.map(analyse_sentiment, text_files)
