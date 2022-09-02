import os
from universal.temporary_datas import coordinates
from world.render import Render


def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")


def reset_data():
    """ Clears the temporary datas stored in the following
        classes: GameObject, Render

        Once the game is restarted this function can be used
        to reset all stored datas to avoid any conflict
        between previous and new game.
    """
    coordinates.clear()
    Render.objects.clear()
