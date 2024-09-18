
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from space_game.middleware import PreserveJSONResponse, json_to_html
from space_game.game import Game

app = FastAPI(default_response_class=PreserveJSONResponse)

# register middleware that automatically uses JINJA templates
# so we only have to write REST functions
# *** Kudos to Tim Weber for finding out! ***
app.middleware("http")(json_to_html)


class LocationData(BaseModel):
    name: str
    image: str
    description: str


class GameData(BaseModel):

    game_id: str
    location: LocationData
    cargo: str|None = None
    crew: list[str] = ["panda"]
    commands: list[str]
    message: str|None = None


def get_game_data(game, message=None) -> GameData:
    return GameData(
        game_id="1",
        location=LocationData(
            name=game.location.name,
            image=game.location.image,
            description=game.location.description,
            ),
        cargo=game.cargo,
        crew=game.crew,
        commands=[cmd.name for cmd in game.get_commands()],
        message=message,
    )

game = None

@app.get("/new_game", response_model=GameData)
def new_game() -> GameData:
    global game
    game = Game()
    return get_game_data(game)


@app.get("/action/{game_id}/{command}")
def action(game_id: str, command: str) -> GameData:
    global game
    msg = "invalid command"
    for cmd in game.get_commands():
        if cmd.name == command:
            msg = cmd.execute()
    return get_game_data(game, msg)


# Also let FastAPI serve the HTMX "frontend" of our application.
app.mount("/", StaticFiles(directory="static", html=True), name="static")
