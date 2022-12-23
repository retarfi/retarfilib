import logging


def get_logger() -> logging.RootLogger:
    # get root logger
    # logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%Y/%m/%d %H:%M:%S', level=logging.INFO)
    logger: logging.Logger = logging.getLogger("__main__")
    logger.setLevel(logging.INFO)
    ch: logging.StreamHandler = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    formatter: logging.Formatter = logging.Formatter(
        fmt="%(asctime)s [%(levelname)s] %(message)s", datefmt="%Y/%m/%d %H:%M:%S"
    )
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger
