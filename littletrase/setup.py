import os

BASE_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
CONN_STRING = "dbname='littletracedb' host='localhost' port='5432' user='traceworker' password='password123'"

# Some simple lcgging configuration.
LOGGING = {
    "version": 1,
    "disable_existing_loggers": 'true',
    "formatters": {
        "simple": {
            "class": "logging.Formatter",
            "datefmt": "%I:%M:%S",
            "format": "%(levelname)-8s;%(name)-15s;%(message)s"
        },
        "verbose": {
            "class": "logging.Formatter",
            "datefmt": "%I:%M:%S",
            "format": "%(levelname)-8s; [%(process)d]; %(threadName)s; %(name)-15s; %(module)s:%(funcName)s;%(lineno)d: %(message)s"
        },
        "multiline": {
            "class": "logging.Formatter",
            "format": "Level: %(levelname)s\nTime: %(asctime)s\nProcess: %(process)d\nThread: %(threadName)s\nLogger: %(name)s\nPath: %(module)s:%(lineno)d\nFunction :%(funcName)s\nMessage: %(message)s\n"
        }
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "multiline", # Choose your console formatter here
            "stream": "ext://sys.stdout"
        }
    },
    "loggers": {},
    "root": {
        "handlers": [ "console" ],
        "level": "DEBUG"
    }
}