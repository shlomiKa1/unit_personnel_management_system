from utils.io import load_json, save_json
from fastapi import HTTPException

def get_all_soldiers():
    soldiers = load_json()
    return soldiers

def get_soldier(id: int):
    soldiers = load_json()
    
    if not soldiers:
        raise HTTPException(404, "There is not soldiers in data")
    
    for soldier in soldiers:
        if soldier["id_Personal"] == id:
            return soldier
    raise HTTPException(500, "ID is not exists")
