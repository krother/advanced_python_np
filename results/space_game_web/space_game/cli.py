"""
Space Traveller - graphical user interface
"""

import sys

from game import Game

# start the game
space_game = Game()
#game_two = Game()  # we could start two games now

while not space_game.is_solved():
    print()
    print("location: ", space_game.location.name)
    print("          ", space_game.location.description)
    print()
    print("cargo   : ", space_game.cargo)
    print("crew    : ", ", ".join(space_game.crew))
    print()

    commands = space_game.get_commands()
    print("Available commands:\n")
    for i, cmd in enumerate(commands, 1):
        print(f"[{i}] {cmd.name}")
    print("[x] Exit")

    key = input("\nenter command: ")
    print("-" * 60)
    if key == "x":
        sys.exit(0)
    else:
        cmd = commands[int(key) - 1]
        message = cmd.execute()

        if message:
            print(f"**{message}**\n")
