import os
from src.csv_utils import remove_duplicates_csv

if __name__ == "__main__":
    base_path = os.path.dirname(__file__)
    file1 = os.path.join(base_path, "work_with_csv", "rmc.csv")
    file2 = os.path.join(base_path, "work_with_csv", "r-m-c.csv")
    result = os.path.join(base_path, "work_with_csv", "result_Kovylin.csv")

    remove_duplicates_csv(file1, file2, result)
