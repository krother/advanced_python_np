
# Session 5: Automated Testing

### Exercise 1: Preparations

Install:

    pip install pytest pytest-cov

### Exercise 2: Run tests

Execute the file `test_words.py` with the `pytest` library:

    pytest

Fix the first test.

### Exercise 3: More tests

Remove the underscore from the next test function.

Re-run the tests and make them pass.

### Exercise 4: Test coverage

Run the test with coverage:

    pytest --cov .

### Exercise 5: Test the space game

Write a test for the space game that:

1. creates a new `Game` object
2. checks that the name of the location is the starting planet
3. executes the first command from the list
4. checks that the location has changed

Run the test and make sure it passes.

### Exercise 6: Another test

Write another test for the space game.

### Exercise 7: Mocking

Examine and run the following code:

    import math
    from unittest.mock import patch

    with patch('math.sin', return_value=42):
        print(math.sin(123))

How could this be useful when writing tests?
