import networkx as nx
from networkx.algorithms import community
from functools import reduce
from networkx.algorithms.community import greedy_modularity_communities


def communities(network):
    nodes = network["nodes"]
    links = network["links"]
    G = nx.Graph()
    # G.add_nodes_from([node["name"] for node in nodes])
    G.add_nodes_from([node["id"] for node in nodes])
    G.add_edges_from([(link["source"], link["target"]) for link in links])
    for n in G:
        G.nodes[n]["name"] = n
    print(nx.info(G), "\n")
    c = list(greedy_modularity_communities(G))
    print(len(c), "communities")
    maxCom = 5
    res = []
    last = []
    for i, cc in enumerate(c):
        if i < maxCom - 1:
            res.append(list(cc))
        else:
            last += (list(cc))
    if last:
        res.append(last)
    return res, G


if __name__ == "__main__":
    import json
    import matplotlib.pyplot as plt
    # network = json.load(open("./test/miserables.json"))
    network = json.load(open("./test/PolBooks.json"))
    # network = json.load(open("./test/epinions_1_percent.json"))
    # network = json.load(open("./test/epinions_5_percent.json"))
    # network = json.load(open("./test/starwars-full-mentions.json"))
    c, G = communities(network)
    print(c)
    # print(len(c))
