import os
import json
from logger_config import logger
from fastapi import HTTPException


FILENAME = "soldiers.json"

def read_json():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r", encoding="utf-8") as file:
            data = json.load(file)
            
            if len(data) == 0:
                logger.warning(f"File {FILENAME} is empty")
            logger.info(f"Return {len(data)} data")
            return data or []
    raise HTTPException(404, "Error file is not exists")