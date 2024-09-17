from location import Location, Puzzle, create_galaxy


class LoadCargoCommand:
    def __init__(self, resource: str):
        self.name = f"collect {resource}"
        self.resource = resource

    def execute(self) -> str:
        """pick up items"""
        global cargo
        cargo = self.resource
        return f"your ship loaded {self.resource}"


class MoveCommand:
    def __init__(self, destination: Location):
        # find out the right word for the command
        transition = (location.type, destination.type)
        if transition == ("planet", "planet"):
            prefix = "warp to"
        elif transition == ("planet", "ship"):
            prefix = "board"
        elif transition == ("ship", "planet"):
            prefix = "back to"
        elif transition == ("planet", "surface"):
            prefix = "beam down to"
        elif transition == ("surface", "planet"):
            prefix = "back to orbit of"
        elif transition == ("surface", "surface"):
            prefix = "go to"
        else:
            prefix = "move to"

        self.name = f"{prefix} {destination.name}"
        self.destination = destination

    def execute(self) -> str:
        global location
        location = self.destination
        return f"moved to {self.destination.name}"


class PuzzleCommand:
    def __init__(self, puzzle: Puzzle):
        self.name = puzzle.action_name

    def execute(self) -> str:
        """pick up items"""
        return solve_puzzle()


# start the game
galaxy = create_galaxy()
location: Location = galaxy["Pandalor"]
cargo: str = ""
crew: list[str] = ["panda"]


def is_solved() -> bool:
    """Returns True when the game is finished"""
    return location.name == "Rainbow portal"


def solve_puzzle() -> str:
    """
    player attempts to puzzle the special effect of the current location.
    Returns a message
    """
    global cargo
    puzzle = location.puzzle
    assert puzzle
    if (
        (puzzle.require_good is None or (cargo == puzzle.require_good))
        and (puzzle.require_crew_member is None or (puzzle.require_crew_member in crew))
    ):
        # player triggers the effect of a puzzle
        if puzzle.deactivate:
            location.puzzle = None
        if puzzle.clear_cargo:
            cargo = ""
        if puzzle.gain_crew_member:
            crew.append(puzzle.gain_crew_member)
        if puzzle.gain_cargo:
            cargo = puzzle.gain_cargo
        if puzzle.gain_connection:
            location.connected_names.append(puzzle.gain_connection)
            location.connected_locs.append(galaxy[puzzle.gain_connection])

        return puzzle.activated_message
    return puzzle.not_activated_message


def get_commands() -> list[MoveCommand | LoadCargoCommand | PuzzleCommand]:
    """
    Returns available commands at a given moment during the game.
    """
    commands: list[MoveCommand | LoadCargoCommand | PuzzleCommand] = []
    # move
    for loc in location.connected_locs:
        commands.append(MoveCommand(destination=loc))

    # load goods
    for resource in location.resources:
        commands.append(LoadCargoCommand(resource))

    # solve puzzles
    if location.puzzle:
        commands.append(PuzzleCommand(location.puzzle))

    return commands
