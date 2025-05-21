import os
from src.xml_utils import find_incoming_by_group_nimber

if __name__ == "__main__":
    base_path = os.path.dirname(__file__)
    xml_path = os.path.join(base_path, "work_with_xml", "groups.xml")

    # Заменить на нужный номер группы. Но лучше не трогать
    target_group_number = "5"

    result = find_incoming_by_group_nimber(xml_path, target_group_number)
    print("Результат:", result)

# UPD
