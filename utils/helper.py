from utils.io import load_json, save_json
from fastapi import HTTPException

def get_all_soldiers():
    soldiers = load_json()
    return soldiers


def get_soldier(id_: int):
    soldiers = load_json()
    
    if not soldiers:
        raise HTTPException(404, "There is not soldiers in data")
    
    for soldier in soldiers:
        if soldier["id_Personal"] == id_:
            return soldier
    raise HTTPException(500, "ID is not exists")


def create_soldier(new_soldier: dict):
    soldiers = load_json()
    soldier_id = max([soldier for soldier in soldiers]) + 1 if soldiers else 1

    new_soldier = {"id": soldier_id, **new_soldier}
    soldiers.update(new_soldier)

    save_json(soldiers)
    # if data:
    #     return True
    # return False

def update_soldier(id_: int, updated_soldier: dict):
    soldiers = load_json()
    
    for soldier in soldiers:
        if soldier["id"] == id_:
            soldiers.update(updated_soldier)
            save_json(soldiers)
            break
    else:
        raise HTTPException(404, "ID soldier is not exists")
    

def delete_soldier(id_: int):
    soldiers = load_json()

    updated_soldiers = [soldier for soldier in soldiers if soldier["id"] != id_]

    if len(soldiers) == len(updated_soldiers):
        raise HTTPException(404, f"ID: {id_} is not found")
    
    soldiers.update(updated_soldiers)
    save_json(soldiers)