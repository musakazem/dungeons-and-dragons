from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer
from sqlalchemy_utils import database_exists, create_database
from logs.config import initiate_logs

logger = initiate_logs("db_config")

# configure here
DB_NAME = ""
PASSWORD = ""
HOST = ""
PORT = ""


base = declarative_base()

url = 'postgresql://postgres:' + PASSWORD + "@" + HOST + ":" + PORT + "/" + DB_NAME  # noqa: E501
engine = create_engine(url, echo=False)


class State(base):

    __tablename__ = 'player_state'

    id = Column(Integer(), primary_key=True)
    x_coordinate = Column(Integer(), nullable=False,  unique=False)
    y_coordinate = Column(Integer(), unique=False, nullable=False)


if not database_exists(engine.url):
    create_database(engine.url)
    logger.info("Created new database")
else:
    engine.connect()
    logger.info("Connected to existing database")

base.metadata.create_all(engine)
