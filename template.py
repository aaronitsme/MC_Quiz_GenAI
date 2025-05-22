import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

list_of_files = [
    "src/__init__.py",
    "src/mcqgenerator/__init__.py",
    "src/mcqgenerator/logger.py",
    "src/mcqgenerator/MCQGenerator.py",
    "src/mcqgenerator/utils.py",
    ".env",
    "setup.py",
    "experiment/trials.ipynb",
    "app.py",
    "template/response.json",
    "data/data.txt",
    "StreamlitApp.py"
]

for xfilepath in list_of_files:
    filepath = Path(xfilepath)
    filedir, filename = os.path.split(xfilepath)
    
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
        logging.info(f"Creating empty files: {filepath}")
    else:
        logging.info(f"{filepath} is already created!")