
from game import Game


def test_move():
    g = Game()
    assert g.current_location == "Pandalor"

    g.get_commands()[0].execute()
    assert g.current_location != "Pandalor"


def test_pickup_cargo():
    g = Game()
    assert g.cargo == ""

    g.get_commands()[2].execute()
    assert g.cargo == "fish"
