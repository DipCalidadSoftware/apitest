import requests


class WordpressRequest:
    def get(self, url):
        response = requests.get(url)
        return response

    @staticmethod
    def post(url, headers, payload):
        response = requests.post(url, headers=headers, data=payload)
        return response
