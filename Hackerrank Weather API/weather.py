import json
import math
import re


class WeatherRecord:
    weather_pattern = re.compile(r'(-?\d+)')
    wind_pattern = re.compile(r'Wind: (\d+)')
    humidity_pattern = re.compile(r'Humidity: (\d+)')

    def __init__(self, name, weather, status):
        self.name = name
        self.weather = int(WeatherRecord.weather_pattern.match(weather).groups()[0])
        self.wind = int(WeatherRecord.wind_pattern.match(status[0]).groups()[0])
        self.humidity = int(WeatherRecord.humidity_pattern.match(status[1]).groups()[0])

    def to_dict(self):
        return {
            'name': self.name,
            'weather': f'{self.weather} degree',
            'status': [
                f'Wind: {self.wind}Kmph',
                f'Humidity: {self.humidity}%'
            ]
        }
