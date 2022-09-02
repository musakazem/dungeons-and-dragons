from db.config import State, engine
from sqlalchemy.orm import sessionmaker
from logs.config import initiate_logs


logger = initiate_logs("db_tools")

session = sessionmaker()
local_session = session(bind=engine)


def save_game(x: int, y: int) -> None:
    """ Opens a session and adds the given coordinates
        to their respective fields in the database.

    Parameters
    ----------
    x: int: x coordinate

    y: int: y coordinate
    """

    new_save = State(x_coordinate=x, y_coordinate=y)

    local_session.add(new_save)

    local_session.commit()

    logger.info("successfully saved game")


def load_game() -> (int, int):
    """ Queries through the last entry of the database entity
        and returns the previously saved coordinates. Returns
        None if entry does not exist.

    Returns
    -------
    None: When entry does not exist

    x_coordinate: int: x coordinate queried from entry

    y_coordinate: int: y coordinate queried from entry

    """

    entry = local_session.query(State).order_by(State.id.desc()).first()

    if entry is None:
        return None
    else:

        logger.info("successfully loaded game")
        return entry.x_coordinate, entry.y_coordinate
