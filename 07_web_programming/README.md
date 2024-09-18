# Session 07: Web Programming

In this session, you will connect a web interface to the `pandas_go_to_space` game.

### Step 1: Installation

Install dependencies with:

    pip install -r requirements.txt

### Step 2: Run the web server

Run the FastAPI server with:

    uvicorn --reload space_game.app:app

Open a browser at `http://localhost:8000/new_game` .

You should see a front page with graphics.

### Step 3: OpenAPI interface

The FastAPI server is self-documenting.
Check the page `http://localhost:8000/docs` .

Try out one of the endpoints (use the **try it out button***).

### Step 4: Code review

Read the code in `space_game/app.py`. Find out:

- how are the URLs of API endpoints defined?
- how is the data structure of the JSON output defined?
- where does the data come from?

### Step 5: Add the game

Copy the code for the game to the `space_game` folder (e.g. from results/).
You need all Python files and the two JSON files with the adventure.

Run the CLI to check if you copied everything.

### Step 6: Connect game and API

To connect the game to the API, you need to:

- import the `Game` class in `app.py`
- use the global variable `game`
- create a `Game` instance in the `new_game()` function. Make it global.
- use attributes of the instance to fill the fields of the `GameData` object

Now you can restart the server with:

    uvicorn --reload space_game.app:app

Use the HTML or JSON interface to check whether you see the actual game data.

### Step 7: Commands

The commands are trickier. To connect them you need to:

- get the list of commands from the game
- add only their **names** to the `GameData` object
- the `/action` endpoint receives the name of a command. You need to go through the list of commands, find the matching name and execute that command in the endpoint.

### Step 8: Edit template

One of the text fields in the HTML page contains a placeholder.
Edit the file `templates/game.html` to insert the description of a location.

### Step 9: A bigger galaxy

In `location.py` the filename for the galaxy JSON file is defined. Change it to the bigger galaxy file.

Now you should have a fully playable adventure.

### Step 10: Read a web page

You could play the game from Python. Try:

    import httpx
    p = httpx.get("http://localhost:8000")
    print(p.status_code)
    print(p.text[:100])

and

    p = httpx.get("http://localhost:8000/new_game")
    print(p.json())

Find out the URL for an action:

    # find url for moves
    p = httpx.get(..)
    print(p.text)

### Step 11: Python Package

The folder `space_game` is a Python package.

To import the modules from anywheere, add the `space_game` folder to the `PYTHONPATH` environment variable.

Try:

    from space_game.game import Game

It should work from any folder.

## License

(c) 2024 Kristian Rother.

contact: `kristian.rother@posteo.de`

Tim Weber, Veit Schiele and Frank Hofmann contributed to the front-end code.

Distributed under the conditions of the MIT License. See LICENSE file.

Artwork has been adopted from the Naev game. See `images/ARTWORK_LICENSE` for details.
