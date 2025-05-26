import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.logger import logger
from utils.test_data import divide


def handle_exception(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            logger.error(f"Exception caught in function '{func.__name__}': {e}")
            return "An exception occurred during the execution of a function"
    return wrapper

divide = handle_exception(divide)


if __name__ == "__main__":
    logger.info(f"Running exception-handling decorator test...")

    print(divide(10,2))
    print(divide(5, 0))