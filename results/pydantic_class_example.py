
# old: dataclasses
# new: pydantic
#  (pip install pydantic)

from pydantic import BaseModel

class QuestionAnswer(BaseModel):

    node_type : str
    id : int
    text: str
    yes_id: int|None = None
    no_id: int|None = None


q = QuestionAnswer(
    node_type="question",
    id = 1,
    text = "is it a snake?",
    yes_id = 2,
    no_id = 3,
)
a = QuestionAnswer(
    node_type = "answer",
    id = 2,
    text = "Python!",
)
print(q)
print(a)
