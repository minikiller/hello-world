import requests as req
import json

res = req.get("https://randomuser.me/api/?results=10")

data = res.json()

for user in data["results"]:
    print(user["name"]["first"])



sdsd

