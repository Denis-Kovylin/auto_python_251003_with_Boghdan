import logging
import pytest

from logger_014_testing import log_event


@pytest.fixture(autouse=True)
def capture_logs(caplog):
    """Автоматически перенастраивает логгер 'log_event' на запись в caplog,
    чтобы не писать в файл."""
    caplog.set_level(logging.DEBUG, logger="log_event")
    yield


def test_log_event_success(caplog):
    log_event("alice", "success")
    records = [r for r in caplog.records if r.name == "log_event"]
    assert len(records) == 1
    assert records[0].levelno == logging.INFO
    assert "Username: alice, Status: success" in records[0].getMessage()


def test_log_event_expired(caplog):
    log_event("david", "expired")
    records = [r for r in caplog.records if r.name == "log_event"]
    assert len(records) == 1
    assert records[0].levelno == logging.WARNING
    assert "Username: david, Status: expired" in records[0].getMessage()


def test_log_event_failed(caplog):
    log_event("vlad", "failed")
    records = [r for r in caplog.records if r.name == "log_event"]
    assert len(records) == 1
    assert records[0].levelno == logging.ERROR
    assert "Username: vlad, Status: failed" in records[0].getMessage()


def test_log_event_unknown_status(caplog):
    log_event("eve", "online")
    records = [r for r in caplog.records if r.name == "log_event"]
    assert len(records) == 1
    assert records[0].levelno == logging.ERROR
    assert "Username: eve, Status: online" in records[0].getMessage()
