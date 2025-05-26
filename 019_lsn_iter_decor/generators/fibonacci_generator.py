import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.logger import logger
from utils.test_data import N_big


def fibonacci_up_to_n(n):
    a = 0
    b = 1
    while a < n:
        yield a
        a, b = b, a + b


if __name__ == "__main__":
    logger.info(f"Generating Fibonacci sequence up to {N_big}...")

    for number in fibonacci_up_to_n(N_big):
        print(number)