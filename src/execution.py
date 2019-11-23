import requests

from src import SERVICE_PORT
from src.model import Execution


def do_get(execution: Execution):
    return requests.get('http://localhost:{}/{}'.format(SERVICE_PORT, execution.path),
                        headers=execution.request.headers)


def do_post(execution: Execution):
    return requests.post('http://localhost:{}/{}'.format(SERVICE_PORT, execution.path),
                         headers=execution.request.headers,
                         data=execution.request.payload)


def do_put(execution: Execution):
    return requests.put('http://localhost:{}/{}'.format(SERVICE_PORT, execution.path),
                        headers=execution.request.headers,
                        data=execution.request.payload)


def execute(execution: Execution):
    return {
        'GET': do_get,
        'POST': do_post,
        'PUT': do_put
    }[execution.method](execution)
