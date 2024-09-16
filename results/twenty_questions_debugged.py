import json
import os
from typing import Any, Literal

NodeKey = Literal["yes", "no", "text"]
TreeNode = dict[NodeKey, Any]

# CHECK: editor plugins for type hints: Pylance

PATH, _ = os.path.split(__file__)
FILENAME = os.path.join(PATH, "questions.json")

print(os.getenv("QUESTION_FILENAME"))

def is_answer(node: TreeNode) -> bool:
    """leaf nodes have only a 'text' attribute"""
    return len(node) == 1


def read_data(filename: str) -> TreeNode:
    f = open(filename)
    return json.load(f)


def play(node: TreeNode) -> None:
    finished: bool = False
    while not finished:
        print(node["text"])

        if is_answer(node):
            finished = True
        else:
            answer = input()
            if answer.upper() in ["YES", "Y"]:
                node = node["yes"]
            else:
                node = node["no"]


tree = read_data(FILENAME)
play(tree)
