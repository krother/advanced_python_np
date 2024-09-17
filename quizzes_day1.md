
## Question 1: Identifying Data Types

Which of the following is a valid example of a tuple in Python? 

A) [1, 2, 3]
B) {'key': 'value'}
C) (1, 2, 3)
D) {1, 2, 3}


## Question 2: Debugging Strategies

Which of the following strategies is most effective for identifying the root cause of an error in a Python script?

A) Adding print statements to trace values
B) Rewriting the entire script from scratch
C) Commenting out random sections of code
D) Ignoring the error and hoping it resolves itself


## Question 3: Type Annotations

What is the correct way to add type annotations to the following Python function?

    def add_numbers(a, b):
        return a + b

A) def add_numbers(a: int, b: int) -> int:
B) def add_numbers(a: str, b: str) -> str:
C) def add_numbers(a: float, b: int) -> int:
D) def add_numbers(a: list, b: dict) -> float:


## Question 4: Running Mypy

What does running mypy on a Python script help with?

A) Formatting the code to follow PEP 8 standards
B) Identifying type-related errors in the code
C) Optimizing the code for faster execution
D) Checking for unused variables


## Question 5: Running Black

What does running black on a Python script do?

A) Executes the script line by line
B) Analyzes the script for logical errors
C) Formats the script to follow PEP 8 style guidelines
D) Converts the script to Python 3 syntax


## Question 6: Implementing Function Parameters

Which of the following function signatures correctly defines a function with two optional parameters in Python? 

A) def my_function(a=1, b=2):
B) def my_function(a, b=2):
C) def my_function(a, b=2, c):
D) def my_function(a=1, b):


## Question 7: Splitting Functions

You are refactoring a large function into smaller, more manageable pieces. What is the main benefit of splitting a function into two?

A) It reduces the size of the code file
B) It improves code reusability and readability
C) It eliminates the need for comments
D) It decreases the execution time of the code


## Question 8: Local vs Global Variables

What will be the output of the following code?

    x = 10
    
    def example():
        x = 5
        print(x)
    
    example()
    print(x)

A) 5 and 10
B) 5 and 5
C) 10 and 10
D) 10 and 5


## Question 9: Adding the __main__ Block

What is the purpose of adding a __main__ block to a Python script?

A) To define a global constant
B) To control the execution of code when the script is run directly
C) To prevent the script from running when imported as a module
D) Both B and C

## Question 10: Raising and Catching Exceptions

Which of the following correctly raises and handles a ZeroDivisionError in Python?

A)

    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("Cannot divide by zero!")

B)

    try:
        result = 10 / 0
    except ValueError:
        print("Cannot divide by zero!")

C)

    try:
        result = 10 / 0
    except:
        print("An error occurred")

D)

    try:
        result = 10 / 0
    except ArithmeticError:
        print("Cannot divide by zero!")
