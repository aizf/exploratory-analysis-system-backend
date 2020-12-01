import json
filename = "11-22_09-17-51"
with open("./save/" + filename + ".json", "r") as f:
    net = json.load(f)

for group in range(0, 5):
    nodes = net["nodes"]

    hashDict = {}

    newNodes = []
    newLinks = []
    newNode = {
        "id": "group_" + str(group),
        "x": 439.4824085901362,
        "y": 151.42019862870643,
        "group": group,
        "size": 0
    }
    count = 0
    for node in nodes:
        _id = node["id"]
        if node["group"] == group:
            count += 1
            newNode["size"] += node["size"]
            hashDict[_id] = True
        else:
            newNodes.append(node)
            hashDict[_id] = False
    # newNode["size"] /= count
    newNodes.append(newNode)

    for link in net["links"]:
        source = link["source"]
        target = link["target"]
        if hashDict[source] and hashDict[target]: continue
        if hashDict[source]:
            link["source"] = "group_" + str(group)
        if hashDict[target]:
            link["target"] = "group_" + str(group)
        newLinks.append(link)

    net = {"nodes": newNodes, "links": newLinks}

with open("./save/" + str(2) + "_" + "PolBooks" + ".json", "w") as f:
    json.dump(net, f)
