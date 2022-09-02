from typing import List
from logs.config import initiate_logs


class World:
    """ Creates a list of lists that simulates a 2D nxn grid
        with a coordinate system.
        Requires one parameter:

        -> world_size

        Parameters
        ----------

        world_size: An integer value to specify world size

    """

    logger = initiate_logs("world_logs")

    def __init__(self, world_size: int):

        self.world_size = world_size + 5
        self.world_map = list()

        self.create_world()

        self.logger.info(f"Initialized a new world with size: {world_size}")

    def create_world(self) -> List[List[str]]:
        """ Creates a list of lists that simulates a 2D nxn grid
            with a coordinate system.

            Returns
            -------
            world_map: List
        """
        buffer_zone = 4
        block_rows = ["_"]*(self.world_size + buffer_zone)

        self.world_map = [block_rows[:] for _ in range(self.world_size + buffer_zone)]  # noqa: E501

        for index_row, row in enumerate(self.world_map):  # Creates a wall around map # noqa: E501

            if index_row == 0 + buffer_zone:
                for i in range(0, self.world_size):
                    self.world_map[index_row][i] = "*"

            self.world_map[index_row][0 + buffer_zone] = "*"
            self.world_map[index_row][self.world_size] = "*"

            if index_row == (self.world_size):
                for i in range(0, self.world_size):
                    self.world_map[index_row][i] = "*"

        return self.world_map

    @property
    def get_map(self) -> List[List[str]]:

        return self.world_map
