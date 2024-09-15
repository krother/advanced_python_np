"""
traverses the tree structure of the 20 question data,
collects the questions and answers in two lists
"""
import json


FILNAME = "../01_python_data_structures/questions.json"

def id_generator():
    """creates infinite id values"""
    id = 0
    while True:
        yield id
        id += 1

def is_answer(node):
    return len(node) == 1

def traverse(node, result, gen):
    # TODO: arrange the lines and indent them correctly
    else:
    if is_answer(node):
    left_id = result[-1][1]
    right_id = result[-1][1]
    result.append(["answer", next(gen), node["text"]])
    result.append(["question", next(gen), node["text"], left_id, right_id])
    traverse(node["yes"], result, gen)
    traverse(node["no"], result, gen)


result = []
tree = json.load(open(FILNAME))
traverse(node=tree, result=result, gen=id_generator())
for item in result:
    print(item)
