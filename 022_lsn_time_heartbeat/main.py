from checker.heartbeat_analyzer import analyze_heartbeat
import os

if __name__ == "__main__":
    log_path = os.path.join("logs", "hblog.txt")
    analyze_heartbeat(log_path)
