import os
import json
from logger_config import logger


FILENAME = "soldiers.json"

def load_json():
    data = []
    if os.path.exists(FILENAME):
        with open(FILENAME, "r", encoding="utf-8") as file:
            data = json.load(file)
            
            if len(data) == 0:
                logger.warning("File '%s' is empty", FILENAME)
            logger.info("Return '%s' soldiers", len(data))
            return data
        

def save_json(soldiers: list[dict]):
    if not soldiers:
        logger.warning("soldiers is empty")

    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(soldiers, f, indent=2)
    logger.info("Save '%s' soldiers", len(soldiers))