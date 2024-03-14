
from pathlib import Path
from loguru import logger

class Settings():
    basedir = Path.cwd()
    rawdir = Path("raw")
    processeddir = Path("processed")
    logdir = basedir / "log"





settings = Settings()
logger.add("logfile.log")