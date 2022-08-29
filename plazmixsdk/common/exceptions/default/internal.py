from ..system import PlazmixError


class PLazmixInternalError(PlazmixError):
    def __init__(self, comment: str = "Internal exceptions"):
        super(PLazmixInternalError, self).__init__(comment)


class PlazmixRuntimeError(PLazmixInternalError): ...


class NotFound(PLazmixInternalError): ...


class ServiceError(PLazmixInternalError): ...
