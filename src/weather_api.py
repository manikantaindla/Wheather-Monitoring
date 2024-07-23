import requests
from src.config import OPENWEATHERMAP_API_KEY

# def get_weather(city):
#     url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHERMAP_API_KEY}"
#     print(f"Requesting URL: {url}")  # Debugging line
#     response = requests.get(url)
#     response.raise_for_status()  # Raise error for HTTP requests with errors
#     return response.json()


def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHERMAP_API_KEY}"
    print(f"Requesting URL: {url}")  # Debugging line
    response = requests.get(url)
    print(f"Response Status Code: {response.status_code}")  # Debugging line
    print(f"Response Content: {response.text}")  # Debugging line
    response.raise_for_status()
    return response.json()
