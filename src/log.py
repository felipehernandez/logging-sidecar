import json

from src import LOG_MODE, DEBUG_LOG_MODE
from src.model import LogEntry, LogMode


def _do_logging(log_entry: LogEntry):
    print(json.dumps(log_entry, default=lambda x: x.__dict__))


def _do_logging_none(log_entry: LogEntry):
    pass


def _do_logging_hit(log_entry: LogEntry):
    log_entry.execution.request = None
    log_entry.execution.response = None

    _do_logging(log_entry)


def _do_logging_request_only(log_entry: LogEntry):
    log_entry.execution.request = None

    _do_logging(log_entry)


def _do_logging_response_only(log_entry: LogEntry):
    log_entry.execution.response = None

    _do_logging(log_entry)


def _do_logging_all(log_entry: LogEntry):
    _do_logging(log_entry)


def do_logging(log_entry: LogEntry):
    log_mode = DEBUG_LOG_MODE if log_entry.execution.debug else LOG_MODE

    {
        LogMode.NONE: _do_logging_none,
        LogMode.HIT: _do_logging_hit,
        LogMode.REQUEST: _do_logging_request_only,
        LogMode.RESPONSE: _do_logging_response_only,
        LogMode.ALL: _do_logging_all,
    }[log_mode](log_entry)
