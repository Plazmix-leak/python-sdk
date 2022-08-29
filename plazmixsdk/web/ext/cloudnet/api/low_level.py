import base64
from json import JSONDecodeError

import requests
from requests import HTTPError

from plazmixsdk.common.exceptions.default.internal import ServiceError


class CloudNetPrimitiveClient:
    def __init__(self, username: str, password: str, endpoint: str):
        self._endpoint = endpoint
        self._auth_token = base64.b64encode(f"{username}:{password}".encode('ascii')).decode("ascii")

    def __request(self, api_method: str):
        try:
            return requests.get(f"{self._endpoint}/api/v1/{api_method}", headers={
                "Accept": "application/json",
                "Authorization": f"Basic {self._auth_token}"
            }).json()
        except JSONDecodeError:
            raise ServiceError("Failed CloudNet get data")
        except HTTPError:
            raise ServiceError("Http error, from cloudNet")

    def fetch_services(self):
        return self.__request("services")