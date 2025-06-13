import logging
import os
import pytest

from logger_014_testing import log_event


class TestLogEvent:
    def test_log_event_success(self):
        log_event("alice", "success")
        with open("login_system.log", "r") as f:
            last_line = f.readlines()[-1]
        assert "Username: alice" in last_line
        assert "Status: success" in last_line
        assert "INFO" in last_line

    def test_log_event_expired(self):
        log_event("bob", "expired")
        with open("login_system.log", "r") as f:
            last_line = f.readlines()[-1]
        assert "Username: bob" in last_line
        assert "Status: expired" in last_line
        assert "WARNING" in last_line

    def test_log_event_failed(self):
        log_event("charlie", "failed")
        with open("login_system.log", "r") as f:
            last_line = f.readlines()[-1]
        assert "Username: charlie" in last_line
        assert "Status: failed" in last_line
        assert "ERROR" in last_line

    def test_log_event_unknown_status(self):
        log_event("eve", "wtf")
        with open("login_system.log", "r") as f:
            last_line = f.readlines()[-1]
        assert "Username: eve" in last_line
        assert "Status: wtf" in last_line
        assert "ERROR" in last_line
