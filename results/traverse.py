"""
traverses the tree structure of the 20 question data,
collects the questions and answers in two lists
"""
import json


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


def traverse(node, result: list[Entry], gen):
    # TODO: arrange the lines and indent them correctly
    if is_answer(node):
        result.append(("answer", next(gen), node["text"], None, None))
    else:
        traverse(node["yes"], result, gen)
        left_id = result[-1][1]
        traverse(node["no"], result, gen)
        right_id = result[-1][1]
        assert type(left_id) == int
        assert type(right_id) == int
        result.append(("question", next(gen), node["text"], left_id, right_id))


data = []
tree = json.load(open(FILNAME))
traverse(node=tree, result=data, gen=id_generator())
for item in data:
    print(item)
