import logging
import os
from datetime import datetime

log_path = os.path.join(os.getcwd(), "log") # Get current working directory

os.makedirs(log_path, exist_ok=True)

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%S')}.log"

LOG_FILEPATH = os.path.join(log_path, LOG_FILE)

logging.basicConfig(level=logging.INFO, filename=LOG_FILEPATH, format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s")