import requests
import json
from pprint import pformat

class DOGApi:
    def __init__(self, address, protocol='https'):
        self.address = address
        self.protocol = protocol

    def send_get_request(self, url, headers=None):
        _url = self.urljoin(self.address, url)
        if not headers:
            headers = {
                'Content-type': 'text/html'
            }
        response = requests.get(_url, headers=headers)
        response.raise_for_status()
        return response

    @staticmethod
    def urljoin(*args):
        return "/".join(map(lambda x: str(x).strip('/'), args))

if __name__ == "__main__":
    # Dog = DOGApi('https://dog.ceo')
    # a = Dog.send_get_request('/api/breeds/list/all')
    # print(pformat(a))
    DOGApi.urljoin("https://dog.ceo/dog-api/", "/breeds/list/all")
