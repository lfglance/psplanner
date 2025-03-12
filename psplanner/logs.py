import logging
from logging.handlers import RotatingFileHandler

from psplanner import config


def configure_logging():
    log_dir = config.LOG_DIRECTORY

    if not log_dir:
        return

    # Access log configuration
    access_log_handler = RotatingFileHandler(
        f"{log_dir}/access.log", maxBytes=10 * 1024 * 1024, backupCount=5
    )
    access_log_handler.setFormatter(
        logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )
    )
    access_logger = logging.getLogger("uvicorn.access")
    access_logger.setLevel(logging.INFO)
    access_logger.addHandler(access_log_handler)

    # Error log configuration
    error_log_handler = RotatingFileHandler(
        f"{log_dir}/error.log", maxBytes=10 * 1024 * 1024, backupCount=5
    )
    error_log_handler.setFormatter(
        logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    )
    error_logger = logging.getLogger("uvicorn.error")
    error_logger.setLevel(logging.ERROR)
    error_logger.addHandler(error_log_handler)

    # Engine log configuration
    log_handler = RotatingFileHandler(
        f"{log_dir}/engine.log", maxBytes=10 * 1024 * 1024, backupCount=5
    )
    log_handler.setFormatter(
        logging.Formatter(
            "%(asctime)s - %(message)s"
        )
    )
    engine_logger = logging.getLogger("engine")
    engine_logger.setLevel(logging.INFO)
    engine_logger.addHandler(log_handler)

    # Optional: Redirect stdout/stderr to logs
    logging.basicConfig(level=logging.INFO, handlers=[
        access_log_handler,
        error_log_handler,
        engine_logger
    ])

def engine_log(message):
    if config.LOG_DIRECTORY:
        engine_logger = logging.getLogger("engine")
        engine_logger.info(message)
    else:
        print(message)