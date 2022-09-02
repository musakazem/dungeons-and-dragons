import logging


def initiate_logs(name: str):
    """ Used to set up loggers in different modules.

    Parameters
    ----------
    name: str
    """

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    fh = logging.FileHandler("logs/logs.log")
    fh.setLevel(logging.DEBUG)

    formatter = logging.Formatter("%(asctime)s - %(module)s - %(levelname)s - %(message)s")  # noqa: E501
    fh.setFormatter(formatter)

    logger.addHandler(fh)

    return logger
