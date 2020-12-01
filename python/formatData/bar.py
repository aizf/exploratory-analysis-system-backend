g = {"nodes": [], "links": []}
import json
with open("./test/starwars-full-interactions.json") as f:
    data=json.load(f)

for node in data["nodes"]:
    d = {}
    d["id"]=node["name"]
    d["size"] = node["value"]
    g["nodes"].append(d)

for link in data["links"]:
    d = {}
    nodes = data["nodes"]
    d["source"] = nodes[link["source"]]["name"]
    d["target"] = nodes[link["target"]]["name"]
    d["weight"] = link["value"]
    g["links"].append(d)

with open("./formatData/starwars-full-interactions.json", "w") as f:
    json.dump(g, f)
