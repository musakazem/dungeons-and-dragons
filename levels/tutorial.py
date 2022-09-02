import game_objects.entities as entity
from world.generator import World
from world.render import Render
from logs.config import initiate_logs


class Tutorial(World):
    """ Defines the layout of the level and positions
        the game objects/entities within the layout.

    Takes previously generated "World" as a parameter.

    Parameters
    ----------
    World: Class imported from world.generator

    """
    logger = initiate_logs("level_logger")

    def __init__(self, world_size: int):

        super().__init__(world_size)

        self.player = entity.Player()
        self.dragon = entity.Dragon()
        self.gate = entity.Gate()
        self.info_trigger = entity.InfoTrigger()
        self.save_trigger = entity.SaveTrigger()

        self.board = Render(self.world_map)
        self.initialize_map()

        self.logger.info("Successfully initialized all objects")

    def initialize_map(self):
        """ Stores all the methods of this class to call
            once an instance of this class is created.
        """
        self.create_layout()
        self.initialize_player()
        self.initialize_dragon()
        self.initialize_gate()
        self.initialize_info_trigger()
        self.initialize_save_trigger()

    def create_layout(self) -> None:
        """ Defines layout(walls/borders) for this level.
        """
        for i in range(8, 18):

            self.world_map[i][8] = "*"
            self.world_map[i][17] = "*"

        for i in range(9, 17):

            self.world_map[8][i] = "*"

        for i in range(8, 12):

            self.world_map[17][i] = "*"

        for i in range(14, 17):

            self.world_map[17][i] = "*"

        self.logger.info("Successfully initialized level layout")

    def initialize_player(self) -> None:
        """ Creates an instance of player game object
            for tutorial level.
        """
        self.player.piece = "X"
        self.player.x = 6
        self.player.y = 12

        self.board.render_obj = self.player

    def initialize_dragon(self) -> None:
        """ Creates an instance of dragon game object
            for tutorial level.
        """

        self.dragon.piece = "D"

        self.dragon.generate_coordinates(9, 9, 16, 14)

        self.board.render_obj = self.dragon

    def initialize_gate(self) -> None:
        """ Creates an instance of gate game object
            for tutorial level.
        """
        self.gate.piece = "G"

        self.gate.generate_coordinates(9, 9, 16, 14)

        self.board.render_obj = self.gate

    def initialize_info_trigger(self) -> None:
        """ Creates an instance of info_trigger game object
            for tutorial level.
        """
        self.info_trigger.piece = "?"

        self.info_trigger.x = 12
        self.info_trigger.y = 18

        self.board.render_obj = self.info_trigger

    def initialize_save_trigger(self) -> None:
        """ Creates an instance of save_trigger game object
            for tutorial level.
        """
        self.save_trigger.piece = "S"

        self.save_trigger.x = 14
        self.save_trigger.y = 18

        self.board.render_obj = self.save_trigger
