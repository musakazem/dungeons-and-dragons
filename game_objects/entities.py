from random import randint

from universal.temporary_datas import coordinates
from game_objects.entity_blueprint import IEntity
from db.tools import save_game
from logs.config import initiate_logs


class Entity(IEntity):
    """ A game object that will occupy the game world.
        Does not require any parameters.
    """
    logger = initiate_logs("entity_logger")

    def __init__(self):

        self.x = int()
        self.y = int()

        self.piece = str()

        self.logger.info("An instance of Entity is created")

    def generate_coordinates(
            self,
            min_x: int, min_y: int,
            max_x: int, max_y: int
            ) -> (int, int):
        """ Randomly generates x and y coorinates for a
            game object.

        Also checks for any conflicts with previous coordinates.

        Parameters
        ----------
        min_x: int: Minimum x range to randomly generate integer

        min_y: int: Minimum y range to randomly generate integer

        max_x: int: Maximum x range to randomly generate integer

        max_y: int: Maximum y range to randomly generate integer

        Returns
        -------
        Returns two integer values as x and y coordinates.
        """
        while True:
            self.x = randint(min_x, max_x)
            self.y = randint(min_y, max_y)

            coordinate = [self.x, self.y]

            if coordinate in coordinates:
                self.loggger.debug(
                    "Coordinate generated with a conflict."
                    + "Retrying attempt..."
                    )
                continue
            else:
                coordinates.append(coordinate)
                break

        self.logger.debug(
            "Successfully generated a coordinate:"
            + f"{self.piece}: ({self.x},{self.y})"
            )

        return self.x, self.y

    @property
    def piece(self) -> str:

        return self._piece

    @piece.setter
    def piece(self, obj_piece: str) -> None:
        """ Sets object placeholder which can be used to render
        the board/map.
        """

        if len(obj_piece) > 1:

            self.logger.error("String length too long")
            raise ValueError("String must be of only one character")

        elif type(obj_piece) is not str:

            self.logger.error("TypeError while setting piece")
            raise TypeError("Must be a string")

        else:

            self._piece = obj_piece

            if obj_piece:

                self.logger.debug(f"Entity instance successfuly set piece as {obj_piece}")  # noqa: E501


class Dragon(Entity):
    """ Creates an instance of a Dragon.
    """

    logger = initiate_logs("dragon_logger")

    def __init__(self):

        super().__init__()

        self.logger.info("A dragon entity has been created")


class Gate(Entity):
    """ Creates an instance of a Gate.
    """
    logger = initiate_logs("Gate")

    def __init__(self):

        super().__init__()

        self.logger.info("A gate entity has been created")


class Player(Entity):
    """ Creates an instance of a Player.
    """
    logger = initiate_logs("player_logger")

    def __init__(self):

        super().__init__()

        self.logger.info("A player entity has been created")


class InfoTrigger(Entity):
    """ Creates an instance of a InfoTrigger.

    When trigger activated, predefined information
    is printed on the terminal.
    """
    logger = initiate_logs("info_logger")

    def __init__(self):
        super().__init__()

        self.logger.info("An info trigger instance has been created")

    def show_info(self, info: str) -> None:
        """ Prints a string variable as information to show to the
            player.

        Parameters
        ----------
        info: str:
        """
        self.logger.info("Player triggered an info instance")
        print("*" * 10)
        print(info)
        print("*" * 10)
        input()


class SaveTrigger(Entity):
    """ Creates an instance to save game.
    """
    logger = initiate_logs("save_trigger")

    def __init__(self):
        super().__init__()

        self.logger.info("A safe trigger instance has been created")

    def save_prompt(self, x: int, y: int) -> None:
        """ Takes x and y coordinates as parameters and
            saves them to a database.

        Parameters
        ----------
        x: int: x coordinate

        y: int: y coordinate
        """
        self.logger.info("Player triggered a save instance")
        player_input = input("Do you want to save? [y/n]")

        if (player_input.lower() == "y"
                or player_input.lower() == "yes"):

            save_game(x, y)
            self.logger.info("Player saved the game")
