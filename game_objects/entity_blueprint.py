from abc import ABC, abstractmethod


class IEntity(ABC):
    """ Defines the backbone/blueprint for an Entity
        class.
    """
    @abstractmethod
    def __init__(self):

        self.x = int()
        self.y = int()

        self.piece = str()

    @abstractmethod
    def generate_coordinates(
            self,
            min_x: int, min_y: int,
            max_x: int, max_y: int
            ) -> (int, int):

        raise NotImplementedError

    @property
    @abstractmethod
    def piece(self):

        raise NotImplementedError

    @piece.setter
    @abstractmethod
    def piece(self, obj_piece):

        raise NotImplementedError
