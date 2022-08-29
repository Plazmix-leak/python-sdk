from abc import ABC, abstractmethod


class ICloudNetObject(ABC):

    @classmethod
    @abstractmethod
    def parse_raw(cls, raw: dict):
        pass
