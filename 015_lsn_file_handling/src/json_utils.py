import os
import json
import logging


def validate_json_files(folder_path: str, log_path: str):
    # логгер сетап
    logging.basicConfig(
        filename=log_path,
        level=logging.ERROR,
        format='%(asctime)s - %(levelname)s - %(message)s',
        force=True
    )
    for filename in os.listdir(folder_path):
        full_path = os.path.join(folder_path, filename)

        try:
            with open(full_path, "r", encoding="utf-8") as f:
                json.load(f)
        except json.JSONDecodeError as e:
            logging.error(f"Файл {filename} не є валідним JSON: {e}")

# UPD
