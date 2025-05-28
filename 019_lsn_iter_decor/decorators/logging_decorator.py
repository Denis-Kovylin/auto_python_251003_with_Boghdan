import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.logger import logger
from utils.test_data import describe_person


def logging_of_function_arguments_and_result(func):
    def wrapper(*args, **kwargs):
        logger.info(f"Function arguments: args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logger.info(f"Function result: {result}")
        return result
    return wrapper


if __name__ == "__main__":
    logger.info(f"Logging function call with arguments and result...")

    describe_person = logging_of_function_arguments_and_result(describe_person)

    describe_person("Den", 40, city="Kyiv", hobby="boxing")