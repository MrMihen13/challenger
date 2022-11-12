import json
import requests

from django.conf import settings


class AlphavantageAPI:
    url = 'https://www.alphavantage.co/query'

    def get_trends(self, symbol: str = 'IBM', interval: int = 60):
        params = f"?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval={interval}min&apikey={settings.ALPHAVANTAGE_APIKEY}"
        return self._send_request(params=params)

    def get_news(self, tickers: str = 'AAPL', topics: str = 'technology', limit: int = 10):
        params = f"?function=NEWS_SENTIMENT&tickers={tickers}&topics={topics}&limit={limit}&apikey={settings.ALPHAVANTAGE_APIKEY}"
        return self._send_request(params=params)

    def _send_request(self, params: str) -> dict:
        response = requests.get(url=self.url + params)
        data = response.json()

        return json.loads(data)
