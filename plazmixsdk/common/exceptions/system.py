class PlazmixError(Exception):
    def __init__(self, comment: str = "System exceptions"):
        self._comment = comment

    def get_comment(self) -> str:
        return self._comment

    def __repr__(self):
        return f"[PlazmixError] {self.__class__.__name__}: {self._comment}"

    __str__ = __repr__
