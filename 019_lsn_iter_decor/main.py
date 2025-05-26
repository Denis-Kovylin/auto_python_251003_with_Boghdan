import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

from utils.logger import logger
from utils.test_data import numbers_list, N_small, N_big, divide, describe_person
from iterators.reverse_iterator import ReverseListIterator
from iterators.even_iterator import EvenNumbersIterator
from generators.even_generator import even_numbers_up_to_n
from generators.fibonacci_generator import fibonacci_up_to_n
from decorators.exception_handler_decorator import handle_exception
from decorators.logging_decorator import logging_of_function_arguments_and_result


def run_demo():
    logger.info("========== DEMO STARTED ==========")

    # Reverse iterator
    logger.info("\n[ITERATOR] ReverseListIterator")
    for item in ReverseListIterator(numbers_list):
        print(item, end=' ')
    print("\n")

    # Even number iterator
    logger.info("\n[ITERATOR] EvenNumbersIterator")
    for num in EvenNumbersIterator(N_small):
        print(num, end=' ')
    print("\n")

    # Even number generator
    logger.info("\n[GENERATOR] even_numbers_up_to_n")
    for num in even_numbers_up_to_n(N_small):
        print(num, end=' ')
    print("\n")

    # Fibonacci generator
    logger.info("\n[GENERATOR] fibonacci_up_to_n")
    for num in fibonacci_up_to_n(N_big):
        print(num, end=' ')
    print("\n")

    # Decorator: exception handler
    logger.info("\n[DECORATOR] handle_exception")
    safe_divide = handle_exception(divide)
    print(safe_divide(10, 2))
    print(safe_divide(5, 0))

    # Decorator: logging
    logger.info("\n[DECORATOR] logging_of_function_arguments_and_result")
    logged_describe = logging_of_function_arguments_and_result(describe_person)
    print(logged_describe("Den", 40, city="Kyiv", hobby="boxing"))

    logger.info("========== DEMO FINISHED ==========")


if __name__ == "__main__":
    run_demo()
