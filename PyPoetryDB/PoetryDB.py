import requests
from .utils import format_response, handle_errors

class API:
    def __init__(self, BASE_URL="https://poetrydb.org"):
        self.BASE_URL = BASE_URL

    def list_authors(self):
        response = requests.get(f"{self.BASE_URL}/authors")
        handle_errors(response)
        authors = format_response(response)
        return authors['authors']
    
    def list_titles(self):
        response = requests.get(f"{self.BASE_URL}/titles")
        titles = format_response(response)
        return titles['titles']
    
    def list_author_titles(self, author):
        response = requests.get(f"{self.BASE_URL}/author/{author}")
        handle_errors(response)
        return format_response(response)
    
    def get_poem(self, title):
        response = requests.get(f"{self.BASE_URL}/title/{title}")
        handle_errors(response)
        return format_response(response)
    
    
