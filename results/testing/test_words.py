"""
tests for the word_counter

run with:

    pytest
"""
import pytest
from words import count_words

# TODO: make all tests work

#
# straightforward test
#
def test_simple():
    assert count_words("hello") == 1


#
# test for error
#
def test_error():
    with pytest.raises(Exception):
        # was before: AttributeError
        # AttributeError is a subclass of Exception
        count_words(777)


#
# test with a fixture
#
@pytest.fixture  # this is a decorator
def zen_text():
    """reads a sample text from a file"""
    # called separately for every test
    print("preparing test")
    with open("zen_of_python.txt") as f:
        yield f.read()
    print("cleaning up")

def test_long(zen_text):  # pytest does name matching to find the fixture
    assert count_words(zen_text) > 100


#
# test with parametrization
#
EXAMPLES = [
    ("", 0),
    ("hello", 1),
    ("hello world", 2),
    ("the quick brown fox jumps over the lazy dog", 9),
    ("are-words-with-hyphens-one-or-many?", 7),
    ("säuerliche Brühe", 2),
    ("123 456 789", 0),
]
@pytest.mark.parametrize("text,nwords", EXAMPLES)
def test_examples(text, nwords):
    assert count_words(text) == nwords
