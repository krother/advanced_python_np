
import json
from typing import Any, Literal

NodeKey = Literal["yes", "no", "text"]
TreeNode = dict[NodeKey, Any]

# define our own error type
class TreeReaderError(Exception): pass

def read_data(filename: str) -> TreeNode:
    try:
        f = open(filename)
        return json.load(f)
    except FileNotFoundError as e:
        raise TreeReaderError(f"the file was not found: {filename}")


if __name__ == '__main__':
    # only run this if this script is run as the main program
    # test code
    print(read_data("mini_questions.json"))
