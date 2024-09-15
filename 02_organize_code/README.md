
# Session 2: Organizing Code

**Goal: refactor the code from session 1**


### Exercise 1: Extract a function

Refactor the code so that it contains a function `read_questions()`
that reads the question file.
Implement proper function parameters and return values.
Add type annotations for both.

Re-run the code and make sure it still works.

### Exercise 2: Another function

Repeat the process for the other part of the code and a function `play()`

#### Reflection questions

* where are local variables in the code
* are there global variables?
* should one avoid global variables in general?

### Exercise 3: Main block

Create a `__main__` block that calls both functions.

Re-run the code and make sure it still works.

### Exercise 4: Importable Module

Create an extra module `questions.py` and move the functions into it.
Import the functions properly.

#### Reflection questions

* what different types of import does Python have?
* where does Python import modules from?
* what is PYTHONPATH?


### Exercise 5: Catch exceptions

If the question file is not found, the program should terminate gently with an error message.
Add a `try.. except` block that catches the `FileNotFoundError`.

Also introduce custom exception `TwentyQuestionError` and raise it if the question set is empty.
