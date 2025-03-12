from os import getenv
from dotenv import load_dotenv


load_dotenv()


# App
SECRET_KEY = getenv("SECRET_KEY", "yyyyyyyyyyyyy")
SERVER_NAME = getenv("SERVER_NAME", "127.0.0.1:5000")
SESSION_DURATION = getenv("SESSION_DURATION", 3600)
QUART_ENV = getenv("QUART_ENV", "development")
TEMPLATES_AUTO_RELOAD = getenv("TEMPLATES_AUTO_RELOAD", True)
DEBUG = getenv("DEBUG", True)
LOG_DIRECTORY = getenv("LOG_DIRECTORY", None)

# Cache
CACHE_HOST = getenv("CACHE_HOST", "127.0.0.1")
CACHE_PORT = getenv("CACHE_PORT", "6379")

# Database
DB_PASS = getenv("DB_PASS", "psplanner")
DB_USER = getenv("DB_USER", "psplanner")
DB_NAME = getenv("DB_NAME", "psplanner")
DB_HOST = getenv("DB_HOST", "127.0.0.1")
DB_PORT = getenv("DB_PORT", "5432")
SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Logging
LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {"default": {
        "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s",
    }},
    "handlers": {
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "default"
        }
    },
    "loggers": {
        "uvicorn.error": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": False,
        },
        "uvicorn.access": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": False,
        }
    },
    "root": {
        "level": "DEBUG",
        "handlers": ["console"],
    }
}
