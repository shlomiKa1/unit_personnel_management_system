from logger_config import logger
from utils.helper import Soldier, get_all_soldiers, get_soldier_by_id, create_soldier, update_soldier, delete_soldier
from fastapi import FastAPI, HTTPException, Request, status
from fastapi.responses import JSONResponse
import json


app = FastAPI()

@app.exception_handler(HTTPException)
def except_http(req: Request, e: HTTPException):
    logger.error(e.detail)
    return JSONResponse(
        status_code=e.status_code,
        content={"detail": e.detail}
    )

@app.exception_handler(FileNotFoundError)
def except_file_not_found(req: Request, e: FileNotFoundError):
    logger.error(e.msg)
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal Server Error"}
    )

@app.exception_handler(json.JSONDecodeError)
def except_json_decode_error(req: Request, e: json.JSONDecodeError):
    logger.error(e.msg)
    raise JSONResponse(
        status_code=500,
        content={"detail": "Internal Server Error"}
    )


@app.get("/api/soldiers", status_code=200)
def get_all_soldiers_endpoint():
    logger.info("Get all soldiers")
    return get_all_soldiers()
    

@app.get("/api/soldiers/{id_}", status_code=200)
def get_soldier_endpoint(id_: int):
    logger.info("Get soldier by ID: '%s'", id_)
    return get_soldier_by_id(id_)
    

@app.post("/api/soldiers", status_code=201)
def create_soldier_endpoint(new_soldier: Soldier):
    logger.info("Create a new soldier")
    create_soldier(new_soldier)
    return {"Message": "Soldier created successfully"}


@app.put("/api/soldiers/{id_}")
def update_soldier_endpoint(id_: int, new_soldier: Soldier):
    logger.info("Update soldier with ID: '%s'", id_)
    update_soldier(id_, new_soldier)
    return {"Message": f"Soldier '{id_}' update successfully"}

@app.delete("/api/soldiers/{id_}")
def delete_soldier_endpoint(id_: int):
    logger.info("Delete soldier by ID: '%s'", id_)
    delete_soldier(id_)
    return {"Message": f"Soldier '{id_}' deleted successfully"}