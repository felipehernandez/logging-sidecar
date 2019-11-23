import os

from src import SERVICE_NAME, NAMESPACE
from src.model import Kubernetes, LogEntry

kubernetes = None


def load(log_entry: LogEntry):
    global kubernetes
    if kubernetes is None:
        import socket

        kubernetes = Kubernetes()
        kubernetes.environment = os.environ.get('FLASK_ENV', 'default')
        kubernetes.namespace = NAMESPACE
        kubernetes.service_name = SERVICE_NAME
        kubernetes.container_id = socket.gethostname()

    log_entry.kubernetes = kubernetes
