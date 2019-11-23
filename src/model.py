import time
from enum import Enum


class Kubernetes:
    namespace: str
    service_name: str
    container_id: str

    environment: str

    def __init__(self, namespace='UNKNOWN',
                 service_name='UNKNOWN',
                 container_id='UNKNOWN',
                 environment='UNKNOWN') -> None:
        super().__init__()
        self.namespace = namespace
        self.service_name = service_name
        self.container_id = container_id

        self.environment = environment


class ExecutionRequest:
    headers: dict
    payload: str

    def __init__(self, headers={}, payload='') -> None:
        super().__init__()
        self.headers = headers
        self.payload = payload


class ExecutionResponse:
    def __init__(self, status=None, headers=None, payload=None, content_type=None):
        self.status = status
        self.headers = headers
        self.payload = payload
        self.content_type = content_type


class Execution:
    path: str
    method: str
    start: time
    finish: time
    elapsed_time: int
    trace: dict
    debug: bool
    request: ExecutionRequest
    response: ExecutionResponse


class LogEntry:
    version: str
    kubernetes: Kubernetes
    execution: Execution

    def __init__(self,
                 version='v1',
                 kubernetes=Kubernetes(),
                 execution=Execution()) -> None:
        super().__init__()
        self.version = version
        self.kubernetes = kubernetes
        self.execution = execution


class LogMode(Enum):
    NONE = 1
    HIT = 2
    REQUEST = 3
    RESPONSE = 4
    ALL = 5

    @classmethod
    def _missing_(cls, value):
        return LogMode.NONE


class DebugMode(Enum):
    NONE = 1
    HEADER = 2
    URL = 3

    @classmethod
    def _missing_(cls, value):
        return DebugMode.NONE
