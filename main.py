from logger_config import logger
from utils.helper import get_all_soldiers
from fastapi import FastAPI, HTTPException
import json


app = FastAPI()

@app.get("/api/soldiers", status_code=200)
def get_all_soldiers_endpoint():
    try:
        return get_all_soldiers()
    except FileNotFoundError:
        logger.error("File is not exists")
        raise HTTPException(404, "File is not found")
    
    except json.JSONDecodeError:
        logger.error("JSON file is empty")
        raise HTTPException(500, "Invalid server error")