import networkx as nx
from networkx.algorithms import community
from functools import reduce
from networkx.algorithms.community import greedy_modularity_communities
import json
import time


def save(network):
    tick = time.strftime("%m-%d_%H-%M-%S", time.localtime())
    with open("./save/" + tick + ".json", "w") as f:
        json.dump(network, f)
    return ""


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    # network = json.load(open("./test/miserables.json"))
    network = json.load(open("./test/PolBooks.json"))
    # network = json.load(open("./test/epinions_1_percent.json"))
    # network = json.load(open("./test/epinions_5_percent.json"))
    # network = json.load(open("./test/starwars-full-mentions.json"))
    c, G = communities(network)
    print(c)
    # print(len(c))
