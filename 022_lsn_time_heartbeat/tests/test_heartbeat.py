import os
import tempfile
from checker.heartbeat_analyzer import analyze_heartbeat


def test_heartbeat_analysis(tmp_path):
    sample_lines = [
        "{ Trade Timestamp 05:00:00 Key TSTFEED0300|7E3E|0400 }",
        "{ Trade Timestamp 04:59:30 Key TSTFEED0300|7E3E|0400 }",  # delta = 30 (ok)
        "{ Trade Timestamp 04:58:00 Key TSTFEED0300|7E3E|0400 }",  # delta = 90 (should log ERROR)
    ]

    # Временный лог-файл
    test_log_path = tmp_path / "test_hb.txt"
    with open(test_log_path, "w", encoding="utf-8") as f:
        for line in sample_lines:
            f.write(line + "\n")

    # Очистим лог-файл
    hb_log_path = os.path.join("logs", "hb_test.log")
    if os.path.exists(hb_log_path):
        open(hb_log_path, "w").close()

    # Анализируем
    analyze_heartbeat(str(test_log_path))

    # Проверим, что лог-файл содержит нужный ERROR
    with open(hb_log_path, "r", encoding="utf-8") as f:
        contents = f.read()

    assert "ERROR" in contents
    assert "90.0 сек" in contents
