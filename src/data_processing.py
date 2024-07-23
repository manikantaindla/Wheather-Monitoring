import pandas as pd

def convert_kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def process_weather_data(data):
    processed_data = {
        "city": data["name"],
        "main": data["weather"][0]["main"],
        "temp": convert_kelvin_to_celsius(data["main"]["temp"]),
        "feels_like": convert_kelvin_to_celsius(data["main"]["feels_like"]),
        "dt": pd.to_datetime(data["dt"], unit='s')
    }
    return processed_data
