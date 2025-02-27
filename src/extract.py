import requests
import json

def get_data_from_api(num_search_pages: int = 1, product: str = 'Carros'):
    url = "https://wilmars-scraper.hf.space/product"
    payload = {
    "product": product,
    "pages":num_search_pages
    }

    response = requests.post(url, data=json.dumps(payload))
    return response.json()

