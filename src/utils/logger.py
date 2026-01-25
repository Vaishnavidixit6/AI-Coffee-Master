import logging
import os
from datetime import datetime

# folder created for logs
LOGS_DIR = "logs"
# create logs directory if it doesn't exist
os.makedirs(LOGS_DIR,exist_ok=True)

# to fetch time and date
LOG_FILE = os.path.join(LOGS_DIR, f"log_{datetime.now().strftime('%Y-%m-%d')}.log")

logging.basicConfig(
    filename=LOG_FILE,
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# to get into about the files being accessed
def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    return logger