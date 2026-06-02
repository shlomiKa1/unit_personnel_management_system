from utils.io import load_json, save_json
from logger_config import logger


def soldier_by_id(id_: int, soldiers: list[dict]):
    # if not soldiers:
    #     raise ("There is not soldiers in data")

    for soldier in soldiers:
        if soldier["id"] == id_:
            logger.info(f"Find user with DI: {id_}")
            return soldier
    raise KeyError(f"ID: {id_} is not found")


def get_all_soldiers():
    soldiers = load_json()
    return soldiers


def get_soldier(id_: int):
    soldiers = load_json()
    return soldier_by_id(id_, soldiers)


def create_soldier(new_soldier: dict):
    soldiers = load_json()
    soldier_id = max([soldier["id"] for soldier in soldiers]) + 1 if soldiers else 1

    new_soldier = {"id": soldier_id, **new_soldier}
    soldiers.append(new_soldier)

    save_json(soldiers)


def update_soldier(id_: int, updated_soldier: dict):
    soldiers = load_json()
    
    for soldier in soldiers:
        if soldier["id"] == id_:
            soldier.update(updated_soldier)
            save_json(soldiers)
            return
    raise KeyError


def delete_soldier(id_: int):
    soldiers = load_json()

    soldier = soldier_by_id(id_, soldiers)
    soldiers.remove(soldier)
    
    save_json(soldiers)