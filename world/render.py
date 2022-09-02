from typing import List
from game_objects.entities import Entity


class Render:
    """Renders specified part of the 'world_map' along with its contents.
         _ _ _ _ _ _ _ _ _ _ _
        |_|_|_|_|_|_|_|_|_|_|_|
        |_|_|_|_|_|_|_|_|_|_|_|
        |_|_|_|_|_|_|_|_|_|_|_|
        |_|_|_|_|_|_|_|_|_|_|_|        _ _ _ _ _
        |_|_|_|_|_|_|_|_|_|_|_| --->  |_|_|_|_|_|
        |_|_|_|_|_|X|_|_|_|_|_|       |_|X|_|_|_|
        |_|_|_|_|_|_|_|_|_|_|_|       |_|_|_|_|_|
        |_|_|_|_|_|_|_|_|_|_|_|       |_|_|_|_|_|
        |_|_|_|_|_|_|_|_|_|_|_|       |_|_|_|_|_|
        |_|_|_|_|_|_|_|_|_|_|_|
                                    render_map(4, 4, 5)

        Parameters
        ----------
        world_map: An iterable as a nested list {List[List]}.
                   Can be acquired from the "World" class.
    """

    objects = dict()

    def __init__(self, world_map: List[List[str]]):

        self.world_map = world_map

    def render_map(self, x: int, y: int, render_range: int) -> None:
        """Prints/renders the indicated part of the 'world_map' according
           to the given parameters.


        Parameters
        ----------
        x : An integer x coordinate that indicates the
            x position to render board.

        y : An integer y coordinate that indicates the
            y position to render board.

        render_range : An integer value that indicates the length
                       to which the map is to be rendered.

        """

        render_list = self.world_map
        render_list = render_list[y:y+render_range]

        for indx, elem in enumerate(render_list):
            render_list[indx] = render_list[indx][x:x+render_range]

        print(" _"*render_range)

        for cell in render_list:
            print("|" + "|".join(cell) + "|")

        return ""

    def render_player(self, player: Entity) -> None:
        """Updates position of the player to render.

           Uses "objects" dictionary to replace previous
           player position with default place holder '_'

        Parameters
        ----------
        player : A game object

        """
        old_coordinates = self.objects["X"]
        x = old_coordinates[0]
        y = old_coordinates[1]

        self.world_map[y][x] = "_"
        self.world_map[player.y][player.x] = "X"

        self.objects["X"] = [
            player.x,
            player.y
        ]

    def follow_player(self, player_instance: Entity) -> None:
        """ Follows the player by rendering the map/board with
            respect to the player's position.

        Parameters
        ----------
        player_instance: Entity:
        """

        x = player_instance.x
        y = player_instance.y

        look_range = 5
        render_range = 11

        render_x = x - look_range
        render_y = y - look_range

        self.render_map(render_x, render_y, render_range)

    @property
    def render_obj(self) -> Entity:
        return self.objects

    @render_obj.setter
    def render_obj(self, obj: Entity) -> None:
        """ Takes object position to render.

            Note: Only used to initialize object positions
                  and cannot be used to update positions.

        Parameters
        ----------
        obj : A game object

        """
        self.objects[obj.piece] = [
                obj.x,
                obj.y
            ]

        self.world_map[obj.y][obj.x] = obj.piece
