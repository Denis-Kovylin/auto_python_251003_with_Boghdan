import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.logger import logger
from utils.test_data import numbers_list


class ReverseListIterator:
    def __init__(self, list_to_revers_iter: list):
        self.list_to_revers_iter = list_to_revers_iter
        self.index = len(list_to_revers_iter)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.list_to_revers_iter[self.index]


if __name__ == "__main__":
    logger.info("Starting ReverseListIterator test...")

    for item in ReverseListIterator(numbers_list):
        print(item)
