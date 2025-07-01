import logging

logger = logging.getLogger("car_tests")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("test_search.log", encoding="utf-8")
console_handler = logging.StreamHandler()

formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
)
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)
