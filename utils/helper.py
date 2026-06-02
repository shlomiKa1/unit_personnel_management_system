from utils.io import load_json, save_json


def get_all_soldiers():
    soldiers = load_json()
    return soldiers