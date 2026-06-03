from logger_config import logger
from utils.helper import Soldier, get_all_soldiers, get_soldier, create_soldier, update_soldier, delete_soldier
from fastapi import FastAPI, HTTPException
import json


app = FastAPI()

@app.get("/api/soldiers", status_code=200)
def get_all_soldiers_endpoint():
    try:
        logger.info("Get all soldiers")
        return get_all_soldiers()
    
    except FileNotFoundError:
        logger.error("File is not exists")
        raise HTTPException(500, "Internal Server Error")
    
    except json.JSONDecodeError:
        logger.error("JSON file is empty")
        raise HTTPException(500, "Invalid Server Error")
    

@app.get("/api/soldiers/{id_}", status_code=200)
def get_soldier_endpoint(id_: int):
    try:
        logger.info("Get soldier by ID: '%s'", id_)
        return get_soldier(id_)
    except ValueError:
        logger.warning("ID: '%s' is not exists", id_)
        raise HTTPException(404, f"ID: '{id_}' is not found")

    except FileNotFoundError:
        logger.error("File is not exists")
        raise HTTPException(500, "Internal Server Error")
    
    except json.JSONDecodeError:
        logger.error("JSON file is empty")
        raise HTTPException(500, "Invalid Server Error")
    

@app.post("/api/soldiers", status_code=201)
def create_soldier_endpoint(new_soldier: Soldier):
    try:
        logger.info("Create a new soldier")
        create_soldier(new_soldier)
        return {"Message": "Soldier created successfully"}
    
    except FileNotFoundError:
        logger.error("File is not exists")
        raise HTTPException(500, "Internal Server Error")
    
    except json.JSONDecodeError:
        logger.error(f"JSON file is empty")
        raise HTTPException(500, "Internal Server Error")
    

@app.put("/api/soldiers/{id_}")
def update_soldier_endpoint(id_: int, new_soldier: Soldier):
    try:
        logger.info("Update soldier with ID: '%s'", id_)
        update_soldier(id_, new_soldier)
        return {"Message": f"Soldier '{id_}' update successfully"}
    
    except ValueError:
        logger.warning("ID: '%s' is not exists", id_)
        raise HTTPException(404, f"ID: '{id_}' is not found")

    except FileNotFoundError:
        logger.error("File is not exists")
        raise HTTPException(500, "Internal Server Error")
    
    except json.JSONDecodeError:
        logger.error("JSON file is empty")
        raise HTTPException(500, "Invalid Server Error")
    

@app.delete("/api/soldiers/{id_}")
def delete_soldier_endpoint(id_: int):
    try:
        logger.info("Delete soldier by ID: '%s'", id_)
        delete_soldier(id_)
        return {"Message": f"Soldier '{id_}' deleted successfully"}
    
    except ValueError:
        logger.warning("ID: '%s' is not exists", id_)
        raise HTTPException(404, f"ID: '{id_}' is not found")

    except FileNotFoundError:
        logger.error("File is not exists")
        raise HTTPException(500, "Internal Server Error")

    except json.JSONDecodeError:
        logger.error("JSON file is empty")
        raise HTTPException(500, "Invalid Server Error")