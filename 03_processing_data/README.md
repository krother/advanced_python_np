
# Session 3: Processing Data with Python

**Goal: read and write data in different formats.**

### Exercise 1: Flatten the tree

Use a small Python program `traverse.py` that reads the `question.json` file and traverses the tree structure.
The program should build a list with all questions and answers.

**Sort the lines in the `traverse()` function.**


### Exercise 2: Lists

Collect the traversed questions and answers in two separate lists:

    questions: [question_id, text, left_id, right_id]

    answers: [anwser_id, text]

You can use continuous numbering for questions and answers.

### Exercise 2: Write tables

Use the `pandas` library to write and read the question/answer data to CSV files and Excel tables.
The provided code sniplets provide a starting point.

Replace `csv` by `excel` to read and write spreadsheets.

### Exercise 3: Read XML

Use the code sniplet to read all questions from the XML data containing any of the following words:

    bird
    fly
    wing
    feather

### Exercise 4: Write JSON

Use the `json` module to write the original tree to a JSON file.

Also write the list resulting from exercise 1 to a JSON file. Compare the results.

### Exercise 5: SQL

Use the code sniplet to write a table to a SQLite database (apart from the SQLAlchemy library, no installation is required).

Write a SQL query to find questions/answers with keywords of your choice.

### Reflection

Create a table with pros and cons of different formats.
