import requests
from weather import WeatherRecord


class Solution:
    def __init__(self, API_URL):
        self.BASE_URL = API_URL

    def weatherStation(self, keyword, max_temp=None):
        params = {
            'name': keyword,
            'page': 1
        }
        total_pages = None

        records: [WeatherRecord] = []

        while total_pages is None or params['page'] <= total_pages:
            data = requests.get(self.BASE_URL, params=params).json()
            total_pages = data['total_pages']
            for record in data['data']:
                parsed_record = WeatherRecord(record['name'], record['weather'], record['status'])
                if max_temp is None or parsed_record.weather <= max_temp:
                    records.append(parsed_record)
            params['page'] += 1

        return [r.to_dict() for r in records]


if __name__ == '__main__':
    BASE_URL = 'https://jsonmock.hackerrank.com/api/weather/search'
    print(Solution(BASE_URL).weatherStation('AB', max_temp=5))
