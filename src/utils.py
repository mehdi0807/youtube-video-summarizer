from langchain.document_loaders import YoutubeLoader
import requests

API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"  #The API URL to the `bert-large-cnn` model in hugging face

def transcript_loader(url: str) -> str:
    """
    This function takes as argument the url of the video 
    and returns the transcript using Langchain YoutubeLoader
    """
    loader = YoutubeLoader.from_youtube_url(url)
    transcript = loader.load()
    return transcript[0].page_content

def summarizer(text: str, headers:str, api_url: str=API_URL) -> str:
    """
    This function takes as argument a text, an API url of the hugging face model (`bert-large-cnn` by default)
    and returns the summarized text
    """
    response = requests.post(api_url, headers=headers, json={"inputs": text})
    return response.json()[0]['summary_text']