import logging.config

from flask import Flask, request

from src import LISTENING_PORT
from src.execution import execute
from src.kubernetes import load as load_kubernetes
from src.log import do_logging
from src.model import LogEntry
from src.request import load as load_request
from src.response import load as load_response

app = Flask(__name__)
logging.getLogger('werkzeug').setLevel(logging.ERROR)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def log(path):
    log_entry = LogEntry()

    load_kubernetes(log_entry)
    load_request(log_entry, request, path)
    response = execute(log_entry.execution)
    response = load_response(log_entry, response)
    do_logging(log_entry)

    return response


if __name__ == '__main__':
    app.run(port=LISTENING_PORT, debug=False)
