from logger_config import logger
from utils.helper import get_all_soldiers
from utils.helper import get_soldier
from utils.helper import create_soldier
from utils.helper import update_soldier
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
    

@app.get("/api/soldiers/{id_}", status_code=200)
def get_soldier_endpoint(id_: int):
    try:
        return get_soldier(id_)
    except KeyError:
        logger.warning("ID is not exists")
        raise HTTPException(400, f"ID: {id_} is not found")

    except FileNotFoundError:
        logger.error("File is not exists")
        raise HTTPException(404, "File is not found")
    
    except json.JSONDecodeError:
        logger.error("JSON file is empty")
        raise HTTPException(500, "Invalid server error")
    

@app.post("/api/soldiers", status_code=201)
def create_soldier_endpoint(new_soldier: dict):
    try:
        create_soldier(new_soldier)
        return {"Messege": "Soldier created successfully"}
    
    except json.JSONDecodeError:
        logger.error(f"File json is empty")
        raise HTTPException(500, "In Server Error")
    

@app.put("/api/soldiers/{id_}")
def update_soldier_endpoint(id_: int, new_soldier: dict):
    try:
        logger.info("Try to update file")
        update_soldier(id_, new_soldier)
        return {"Message": f"Soldier update successfully {id_}"}
    
    except KeyError:
        logger.warning("ID is not exists")
        raise HTTPException(400, f"ID: {id_} is not found")

    except FileNotFoundError:
        logger.error("File is not exists")
        raise HTTPException(404, "File is not found")
    
    except json.JSONDecodeError:
        logger.error("JSON file is empty")
        raise HTTPException(500, "Invalid server error")