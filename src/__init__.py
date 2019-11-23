import os

from src.model import LogMode, DebugMode

from kubernetes_downward_api import parse

# Kubernetes
metadata = {}
try:
    metadata = parse(['/etc/podinfo'])
except:
    pass

NAMESPACE = metadata.get('namespace', 'UNKNOWN')
print('Namespace : {}'.format(NAMESPACE, ))

SERVICE_NAME = metadata.get('labels', {'app': 'UNKNOWN'}).get('app', 'UNKNOWN')
print('Service name : {}'.format(SERVICE_NAME, ))

POD = metadata.get('pod_name', 'UNKNOWN')
print('Pod id : {}'.format(POD, ))

# Service configuration
ENVIRONMENT = os.environ.get('FLASK_ENV', 'default')
print('Environment: {}'.format(ENVIRONMENT))

LISTENING_PORT = int(os.environ.get('LISTENING_PORT', '5001'))
print('Listening port: {}'.format(LISTENING_PORT))

SERVICE_PORT = int(os.environ.get('SERVICE_PORT', '5000'))
print('Service port: {}'.format(SERVICE_PORT))

LOG_MODE = LogMode[os.environ.get('LOG_MODE', 'NONE')]
print('Log mode: {}'.format(LOG_MODE.name))
DEBUG_LOG_MODE = LogMode[os.environ.get('DEBUG_LOG_MODE', 'NONE')]
print('Debug log mode: {}'.format(DEBUG_LOG_MODE.name))

DEBUG_MODE = DebugMode[os.environ.get('DEBUG_MODE', 'NONE')]
print('Debug mode: {}'.format(DEBUG_MODE.name))

TRACEABLE_HEADERS = [s.lstrip() for s in os.environ.get('TRACEABLE_HEADERS', '').split(',')]
print('Traceable headers: {}'.format(TRACEABLE_HEADERS))
