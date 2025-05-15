import xml.etree.ElementTree as ET
import logging


def find_incoming_by_group_nimber(xml: str, target_number: str):
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        force=True
    )

    tree = ET.parse(xml)
    root = tree.getroot()

    for group in root.findall("group"):
        number_elem = group.find("number")
        if number_elem is not None and number_elem.text == target_number:
            incoming_elem = group.find("timingExbytes/incoming")
            if incoming_elem is not None:
                logging.info(f"Значення incoming для групи {target_number}: {incoming_elem.text}")
                return incoming_elem.text

    logging.error(f"Група з номером {target_number} не знайдена або не має поля incoming.")
    return None

    pass
