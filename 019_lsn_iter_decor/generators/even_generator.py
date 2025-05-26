import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.logger import logger
from utils.test_data import N_small


def even_numbers_up_to_n(n):
    for i in range(n):
        if i % 2 == 0:
            yield i


if __name__ == "__main__":
    logger.info(f"Generating even numbers up to {N_small}...")

    even_numbers_up_to_n(N_small)
    for number in even_numbers_up_to_n(N_small):
        print(number)
