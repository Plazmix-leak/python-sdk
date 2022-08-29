from ._icloud_object import ICloudNetObject


class CloudServiceNet(ICloudNetObject):
    def __init__(self, online: bool, players_count: int, name: str, number: int = 0):
        self.online: bool = online
        self.players_count: int = players_count
        self.name = name
        self.number = number

    @property
    def title(self):
        return f"{self.name}-{self.number}"

    @classmethod
    def parse_raw(cls, raw: dict):
        properties: dict = raw.get("properties", {})
        configuration: dict = raw.get("configuration", {})
        service_id: dict = configuration.get("serviceId", {})
        online_state = properties.get("Online", False)
        players = properties.get("Online-Count", 0)
        service_name = service_id.get("taskName", "unknown")
        number = service_id.get("id", 0)
        return cls(online_state, players, service_name, number)