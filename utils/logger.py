import logging


def setup_logger(name, log_file, level=logging.INFO):
    """
    Setup a logger with specified name, log file, and logging level.

    Args:
        name (str): The name of the logger.
        log_file (str): The path to the log file.
        level (int): The logging level. Defaults to logging.INFO.

    Returns:
        logging.Logger: The configured logger object.
    """
    handler = logging.FileHandler(log_file)
    handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger
