
import re

def count_words(text: str) -> int:
    """returns the number of words in a piece of text"""
    separators = " -\n;:.,?!"
    for digit in "0123456789":
        text = text.replace(digit, "")
    text = text.strip()  # remove whitespace left and right
    if text == "":
        return 0
    lengths = [   # list comprehension
        len(text.split(sep))
        for sep in separators
    ]
    return max(lengths)

def count_words(text: str) -> int:
    return len(re.findall("[a-zäöüß]+", text, re.IGNORECASE))
