import pandas as pd
import json

with open('123.json',encoding="UTF-8") as file:
    data = json.load(file)

print(data["color"])
print(data["number"])
print(data["string"])
