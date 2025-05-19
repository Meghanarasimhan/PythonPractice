import json

with open("config.json", "r") as f:
    config=json.load(f)
print(config["host"])

import configparser

config=configparser.ConfigParser()
config.read("config.ini")
print(config["database"]["host"])
