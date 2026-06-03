from utils.io import load_json, save_json
from logger_config import logger
from fastapi import HTTPException
from pydantic import BaseModel


class Soldier(BaseModel):
    id: int
    name: str
    email: str
    address: str


def get_all_soldiers():
    soldiers = load_json()
    return soldiers


def get_soldier_by_id(id_: int):
    soldiers = load_json()

    for soldier in soldiers:
        if soldier["id"] == id_:
            logger.info("Find user with DI: '%s'", id_)
            return soldier
    raise HTTPException(404, f"ID: '{id_}' is not found")


def create_soldier(new_soldier: Soldier):
    soldiers = load_json()
    soldier_id = max([soldier["id"] for soldier in soldiers]) + 1 if soldiers else 1

    new_soldier = {"id": soldier_id, **new_soldier}
    soldiers.append(new_soldier)

    save_json(soldiers)


def update_soldier(id_: int, updated_soldier: Soldier):
    soldiers = load_json()
        
    soldier = get_soldier_by_id(id_)
    soldier.update(updated_soldier)

    save_json(soldiers)


def delete_soldier(id_: int):
    soldiers = load_json()

    soldier = get_soldier_by_id(id_, soldiers)
    soldiers.remove(soldier)
    
    save_json(soldiers)