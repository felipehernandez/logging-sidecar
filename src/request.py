import time

from flask import request

from src import TRACEABLE_HEADERS, DEBUG_MODE
from src.model import ExecutionRequest, LogEntry, Execution, DebugMode


def _debug_mode(headers, path: str):
    if DebugMode.NONE is DEBUG_MODE:
        return False, path

    if DebugMode.HEADER is DEBUG_MODE:
        return 'debug' in headers.keys(), path

    if DebugMode.URL is DEBUG_MODE:
        if path.startswith('debug'):
            return True, path[6:]
        else:
            return False, path


def load(log_entry: LogEntry, request: request, path: str):
    execution = Execution()
    execution.start = time.time()
    execution.method = request.method
    headers = {key: request.headers[key] for key in request.headers.keys()}
    execution.debug, execution.path = _debug_mode(headers, path)
    execution.request = ExecutionRequest()

    execution.request.headers = headers

    if request.data:
        execution.request.payload = request.data

    execution.trace = {key: request.headers[key] for key in request.headers.keys() if key in TRACEABLE_HEADERS}

    log_entry.execution = execution
