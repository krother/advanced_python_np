
# Session 1: Python Data Structures and Operations

**Goal: debug a Python script**

### Exercise 1: Debug

Execute the program `twenty_questions.py` with

    python twenty_questions.py

You should see that there is at least one bug.
Find and fix all bugs you can find together.

#### Reflection Questions

* What debugging strategies did you use in the process?
* what other techniques for finding bugs do you know?
* why do programmers create bugs?

### Exercise 2: Data types

Discuss the following:

* Which Python data types can you find in the program?
* Which other Python data types do you know?

### Exercise 4: Type annotations

Add type annotations to the function arguments and return values.
Also add type annotations for the most important variables.

Re-run the code and make sure it still works.

*Does the program also work if you deliberately use a **wrong** type?

#### Exercise 5: Type checker

Install a Python type checker with

    pip install mypy

Then check the types with 

    mypy twenty_questions.py

### Exercise 6: Code linter

Clean up the code by running:

    black twenty_questions.py
