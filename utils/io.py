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
                logger.warning(f"File {FILENAME} is empty")
            logger.info(f"Return {len(data)} soldiers")
            return data
    raise FileNotFoundError("Error file is not exists")


def save_json(soldiers: list[dict]):
    if not soldiers:
        logger.warning("soldiers is empty")

    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(soldiers, f, indent=2)
    logger.info(f"Save {len(soldiers)} soldiers")

