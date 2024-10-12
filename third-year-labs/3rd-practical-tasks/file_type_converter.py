import json
import xml.etree.ElementTree as ET


def convert_dictionary_to_json(dictionary):
    return json.dumps(dictionary)


def convert_dictionary_to_xml(dictionary, root_name):
    root = ET.Element(root_name)
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    return root
