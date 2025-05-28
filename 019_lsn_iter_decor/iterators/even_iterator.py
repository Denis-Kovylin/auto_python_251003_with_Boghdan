import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.logger import logger
from utils.test_data import N_small


class EvenNumbersIterator:
    def __init__(self, N):
        self.n = N
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.n:
            raise StopIteration
        else:
            even_number = self.current
            self.current += 2
        return even_number


if __name__ == "__main__":
    logger.info("Starting EvenNumbersIterator test...")


    my_range = EvenNumbersIterator(N_small)
    for num in my_range:
        print(num)