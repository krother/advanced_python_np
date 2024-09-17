"""
traverses the tree structure of the 20 question data,
collects the questions and answers in a list
and writes to a XML file
"""

import json
import xml.etree.ElementTree as ET

FILNAME = "../01_python_data_structures/questions.json"

Entry = tuple[str, int, str, int, int]


def id_generator():
    """creates infinite id values"""
    id = 0
    while True:
        yield id
        id += 1


def is_answer(node):
    return len(node) == 1


def traverse(node, element, gen):
    if is_answer(node):
        answer = ET.SubElement(element, "Answer")
        answer.set("id", str(next(gen)))
        answer.text = node["text"]
    else:
        question = ET.SubElement(element, "Question")
        question.set("id", str(next(gen)))
        question.text = node["text"]
        yes = ET.SubElement(question, "yes")
        traverse(node["yes"], yes, gen)
        no = ET.SubElement(question, "no")
        traverse(node["no"], no, gen)


data = ET.Element("AnimalGuessingGame")
tree = json.load(open(FILNAME))
traverse(node=tree, element=data, gen=id_generator())
for item in data:
    print(item)

b_xml = ET.tostring(data)
with open("QA.xml", "wb") as f:
    f.write(b_xml)
