"""
Locations in the space game can be plantes, spaceships or buildings,
anywhere a player can go.

They provide goods or crew members or open new paths,
some of these require that the player already has certain things. 
"""
import json
import os
from typing import Optional

from pydantic import BaseModel

# provides the absolute path to the current directory
# (useful to load non-python static files)
BASE_PATH = os.path.split(__file__)[0]

#DEFAULT_GALAXY = os.path.join(BASE_PATH, "mini_galaxy.json")
DEFAULT_GALAXY = os.path.join(BASE_PATH, "galaxy_EN.json")


class Puzzle(BaseModel):
    """
    Conditions and effects of puzzles at a location
    """

    # before a puzzle is triggered
    action_name: str
    require_good: str | None = None
    require_crew_member: str | None = None
    activated_message: str
    not_activated_message: str

    # when a puzzle is triggered
    clear_cargo: str | None = None
    gain_crew_member: str | None = None
    gain_cargo: str | None = None
    gain_connection: str | None = None
    deactivate: bool = True


class Location(BaseModel):
    """
    Planets, spaceships and special places on the ground
    """

    galaxy: dict
    name: str
    description: str
    image: str
    type: str = "planet"
    connected_names: list[str]
    connected_locs: list["Location"] = []
    resources: list[str] = []
    puzzle: Optional[Puzzle] = None

    def __repr__(self) -> str:
        """returns string representation of this location"""
        puzzle = "yes" if self.puzzle else "no"
        return f"<{self.name}: {self.type}; provides {self.resources}; puzzle: {puzzle}>"

    def add_connection(self, location) -> None:
        """helper function to create a fully connected graph of locations"""
        self.connected_locs.append(location)


def create_galaxy(filename: str = DEFAULT_GALAXY) -> dict[str, Location]:
    """Loads entire playing environment from a JSON file"""
    with open(filename, encoding="utf-8") as file:
        j = json.load(file)

    galaxy: dict[str, Location] = {}
    locs = [Location(galaxy=galaxy, **loc) for loc in j]
    # builds connection graph
    for location in locs:
        location.galaxy = galaxy
        galaxy[location.name] = location
        for targetname in location.connected_names:
            target = None
            for loc2 in locs:
                if loc2.name == targetname:
                    target = loc2
                    break
            if target is None:
                raise ValueError(
                    f"connection not found when building galaxy for '{targetname}'"
                )
            location.add_connection(target)

    return galaxy
