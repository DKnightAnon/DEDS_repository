
from pathlib import Path
from loguru import logger
import socket

class Settings():
    basedir = Path.cwd()
    rawdir = Path("raw")
    processeddir = Path("processed")
    logdir = basedir / "log"
    
    database = 'GreatOutdoorsDW'
    DB = {
        'servername': socket.gethostname()[:15]+'\\SQLEXPRESS',
        'database' : database
    }

    



settings = Settings()
logger.add("logfile.log")

# print(settings.DB["servername"])