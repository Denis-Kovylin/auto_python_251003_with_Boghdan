import logging
import os
import pytest

from logger_014_testing import log_event



def test_log_event_success():
    open("login_system.log", "w").close()
    log_event("alice", "success")
    with open("login_system.log", "r") as f:
        last_line = f.readlines()[-1]
    assert "Username: alice, Status: success" in last_line

def test_log_event_expired():
    open("login_system.log", "w").close()
    log_event("bob", "expired")
    with open("login_system.log", "r") as f:
        last_line = f.readlines()[-1]
    assert "Username: bob, Status: expired" in last_line

def test_log_event_failed():
    open("login_system.log", "w").close()
    log_event("charlie", "failed")
    with open("login_system.log", "r") as f:
        last_line = f.readlines()[-1]
    assert "Username: charlie, Status: failed" in last_line

def test_log_event_unknown_status():
    open("login_system.log", "w").close()
    log_event("eve", "wtf")
    with open("login_system.log", "r") as f:
        last_line = f.readlines()[-1]
    assert "Username: eve, Status: wtf" in last_line
