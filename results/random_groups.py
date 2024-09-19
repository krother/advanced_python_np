"""
randomize groups

Preparations:

    pip install faker
"""
import random
from pprint import pprint

from faker import Faker

f = Faker()
participants = [f.name() for _ in range(9)]

result = {"A": [], "B": [], "C": []}

for person in participants:
    group = random.choice(list(result.keys()))
    result[group].append(person)
pprint(result)

# alternative
random.shuffle(participants)
print(participants)
