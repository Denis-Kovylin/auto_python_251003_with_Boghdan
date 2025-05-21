import os
from src.json_utils import validate_json_files

if __name__ == "__main__":
    base_path = os.path.dirname(__file__)
    json_folder = os.path.join(base_path, "work_with_json")
    log_file = os.path.join(base_path, "json_Kovylin.log")

    validate_json_files(json_folder, log_file)

# UPD
