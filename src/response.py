import time
from http import HTTPStatus

from flask import Response

from src.model import ExecutionResponse, LogEntry, Execution


def _time_in_millis(complex_time):
    return int(round(complex_time * 1000))


def _calculate_elapsed_time(execution: Execution):
    return _time_in_millis(execution.finish) - _time_in_millis(execution.start)


def load(log_entry: LogEntry, response):
    if response is not None:
        headers = {}
        for header in response.headers.keys():
            headers[header] = response.headers[header]

        execution = log_entry.execution
        execution.finish = time.time()
        execution.elapsed_time = _calculate_elapsed_time(execution)
        execution.response = ExecutionResponse()
        execution.response.status = response.status_code
        execution.response.content_type = response.headers['Content-Type']
        execution.response.headers = {key: response.headers[key] for key in response.headers.keys()}
        execution.response.payload = response.text

        return Response(execution.response.payload,
                        status=execution.response.status,
                        mimetype=execution.response.content_type,
                        headers=execution.response.headers)
    else:
        return Response('ERROR',
                        status=HTTPStatus.INTERNAL_SERVER_ERROR,
                        mimetype='text/html',
                        headers={key: response.headers[key] for key in response.headers.keys()})
