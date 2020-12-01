g = {"nodes": [], "links": []}

with open("./formatData/nodes.txt") as f:
    for line in f.readlines():
        _id = line.split(" ", 1)[1][1:-2]
        g["nodes"].append({"id": _id})
        # print(node)
# group
with open("./formatData/others.txt") as f:
    i = 0
    for line in f.readlines():
        group = int(line)
        g["nodes"][i]["group"] = group
        i += 1

with open("./formatData/links.txt") as f:
    for line in f.readlines():
        source, target = [
            g["nodes"][int(s) - 1]["id"] for s in line.split(" ", 1)
        ]
        g["links"].append({"source": source, "target": target})

# print(g)
import json
with open("./formatData/res.json", "w") as f:
    json.dump(g, f)
