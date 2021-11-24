import re
import pytest
from os import path
import logging

slugify = re.compile(r"[^a-zA-Z0-9_\-]")
logger =logging.getLogger(__name__)

def test_aa(request, caplog):
    
    aa = slugify.sub("-", request.node.name)
    logger.info(request.node.name)
    assert aa == "test_aa"
    assert 1

def test_monke(monkeypatch):
    def return_true(path):
        return True
    monkeypatch.setattr(path, "exists", return_true)
    a = path.exists("/cc/ddd/fff")
    assert a is True

def test_log_message(caplog):
    caplog.messages       # -> list of format-interpolated log messages
    caplog.text           # -> string containing formatted log output
    caplog.records        # -> list of logging.LogRecord instances
    caplog.record_tuples