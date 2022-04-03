import json
from pprint import pprint


def users_info():
    with open("users.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        candidates = {}
        for i in data:
            candidates[i["id"]] = i
        return candidates


users_info()
