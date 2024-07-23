import unittest
# from src/weather_api import get_weather
from src.weather_api import get_weather

from src.data_processing import convert_kelvin_to_celsius

class TestWeatherApp(unittest.TestCase):
    def test_get_weather(self):
        data = get_weather("Delhi")
        self.assertIn("main", data)

    def test_convert_kelvin_to_celsius(self):
        self.assertAlmostEqual(convert_kelvin_to_celsius(273.15), 0)

if __name__ == "__main__":
    unittest.main()
