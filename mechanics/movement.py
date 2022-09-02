from typing import List
from game_objects.entities import Entity


class Movement:
    """Applies movement mechanics to a game object"""

    def __init__(self, game_obj: Entity):

        self.game_obj = game_obj

    @property
    def move(self) -> (int, int):
        return self.game_obj.x, self.game_obj.y

    @move.setter
    def move(self, direction: str) -> None:
        """ Sets new player coordinates according
            to specified directions.

        Parameters
        ----------
        direction : a string value that is limited to,

            -> 'up', 'down', 'left', 'right'

        """
        valid_params = ("up", "down", "left", "right")

        if direction in valid_params:
            if direction == "up":
                self.move_up()

            elif direction == "down":
                self.move_down()

            elif direction == "left":
                self.move_left()

            elif direction == "right":
                self.move_right()
        else:
            raise TypeError("Did not recieve a valid parameter"
                            + "(up, down, left, right)")

    def move_up(self):

        self.game_obj.y -= 1

    def move_left(self):

        self.game_obj.x -= 1

    def move_right(self):

        self.game_obj.x += 1

    def move_down(self):

        self.game_obj.y += 1


def positional_awareness(
        game_obj: Entity,
        world_map: List[List[str]]) -> List[str]:

    """ Checks for any boundaries one cell from each direction
        of a game object's position.

    Parameters
    ----------
    obj: A game object. Used to extrace object coordinates.

    world_map: List: a list of lists that simulates a 2D nxn grid
                     with a coordinate system.

    Returns
    -------
    Returns all possible directions the player can move as
    strings in a list.
    """

    x = game_obj.x
    y = game_obj.y

    options = list()

    check_up = y - 1
    check_down = y + 1
    check_left = x - 1
    check_right = x + 1

    if world_map[check_up][x] is not "*":
        options.append("UP")
    
    if world_map[check_down][x] is not "*":
        options.append("DOWN")
    
    if world_map[y][check_right] is not "*":
        options.append("RIGHT")
    
    if world_map[y][check_left] is not "*":
        options.append("LEFT")

    return options
