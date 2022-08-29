from typing import List

from .obj import CloudServiceNet
from ..low_level import CloudNetPrimitiveClient


class CloudNetClient:
    def __init__(self, username: str, password: str, endpoint: str):
        self._low_level = CloudNetPrimitiveClient(username=username,
                                                  password=password,
                                                  endpoint=endpoint)

    def get_services(self) -> List[CloudServiceNet]:
        raw_data = self._low_level.fetch_services()

        result = []
        for raw_service in raw_data:
            result.append(CloudServiceNet.parse_raw(raw_service))
        return result
