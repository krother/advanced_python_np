"""
when Python creates an instance of a class:
1. calls __new__ that creates the instance (you never see this)
2. calls the constructor __init__ to define attributes
"""
from location import Location, Puzzle, create_galaxy
from abc import ABC, abstractmethod  # Abstract Base Class


class Command(ABC):

    def __init__(self, game, name):
        self._game = game
        self.name = name

    @abstractmethod
    def execute(self) -> str:
        """every subclass of Command is expected to overwrite this"""
        pass



class LoadCargoCommand(Command):
    def __init__(self, game, resource: str):
        # traditional way to create an instance
        super().__init__(game=game, name=f"collect {resource}")
        self.resource = resource
    
    def __del__(self):
        # destructor
        #print("DESTRUCTOR CALLED")
        pass

    def __repr__(self) -> str:
        # returns a string representation of the instance
        return f"LoadCargoCommand: {self.name} ({self.resource})"

    def execute(self) -> str:
        """pick up items"""
        # a method inside the class
        self._game.cargo = self.resource
        return f"your ship loaded {self.resource}"


class MoveCommand(Command):
    def __init__(self, game, destination: Location):
        # find out the right word for the command
        transition = (game.location.type, destination.type) # needs the location of the player
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

        super().__init__(game=game, name=f"{prefix} {destination.name}")
        self.destination = destination

    def execute(self) -> str:
        self._game.location = self.destination
        return f"moved to {self.destination.name}"


class PuzzleCommand(Command):
    def __init__(self, game, puzzle: Puzzle):
        super().__init__(game, puzzle.action_name)

    def execute(self) -> str:
        """
        player attempts to puzzle the special effect of the current location.
        Returns a message
        """
        puzzle = self._game.location.puzzle
        assert puzzle  # data integrity check: puzzle must not be None
        if (
            (puzzle.require_good is None or (self._game.cargo == puzzle.require_good))
            and (puzzle.require_crew_member is None or (puzzle.require_crew_member in self._game.crew))
        ):
            # player triggers the effect of a puzzle
            if puzzle.deactivate:
                self._game.location.puzzle = None
            if puzzle.clear_cargo:
                self._game.cargo = ""
            if puzzle.gain_crew_member:
                self._game.crew.append(puzzle.gain_crew_member)
            if puzzle.gain_cargo:
                self._game.cargo = puzzle.gain_cargo
            if puzzle.gain_connection:
                self._game.location.connected_names.append(puzzle.gain_connection)
                self._game.location.connected_locs.append(self._game.galaxy[puzzle.gain_connection])

            return puzzle.activated_message
        return puzzle.not_activated_message


class Game:

    def __init__(self):
        """start the game"""
        self.galaxy = create_galaxy()
        self.location: Location = self.galaxy["Pandalor"]
        self.cargo: str = ""
        self.crew: list[str] = ["panda"]

    @property
    def current_location(self):
        return self.location.name

    def is_solved(self) -> bool:
        """Returns True when the game is finished"""
        return self.location.name == "Rainbow portal"

    def get_commands(self) -> list[Command]:
        """
        Returns available commands at a given moment during the game.
        """
        commands: list[Command] = []
        # move
        for loc in self.location.connected_locs:
            commands.append(MoveCommand(game=self, destination=loc))

        # load goods
        for resource in self.location.resources:
            commands.append(LoadCargoCommand(game=self, resource=resource))

        # solve puzzles
        if self.location.puzzle:
            commands.append(PuzzleCommand(game=self, puzzle=self.location.puzzle))

        return commands
