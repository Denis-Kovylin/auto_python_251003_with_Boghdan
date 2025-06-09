import logging
import os

log_dir = os.path.join(os.path.dirname(__file__), "..", "logs")
log_file = os.path.join(log_dir, "hb_test.log")

os.makedirs(log_dir, exist_ok=True)

logger = logging.getLogger("heartbeat")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(log_file, mode='w', encoding='utf-8')
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)

logger.handlers.clear()
logger.addHandler(file_handler)
logger.addHandler(console_handler)
