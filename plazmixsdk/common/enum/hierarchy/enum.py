from enum import Enum

from plazmixsdk.common.exceptions.default.internal import NotFound


class HierarchyEnum(Enum):
    @classmethod
    def get_from_technical_name(cls, technical_name):
        for name, value in cls.__dict__.items():
            try:
                if value.value.get_technical_name == technical_name:
                    return value
            except AttributeError:
                continue
        raise NotFound("An element with this technical name was not found")



