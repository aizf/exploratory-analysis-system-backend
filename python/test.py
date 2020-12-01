import networkx as nx
from networkx.algorithms import community
from functools import reduce
from networkx.algorithms.community import greedy_modularity_communities
from karateclub import EgoNetSplitter


def network_centrality(network):
    nodes = network["nodes"]
    links = network["links"]
    isDirected = network.get("isDirected", False)
    if isDirected:
        G = nx.DiGraph()
    else:
        G = nx.Graph()
    # G.add_nodes_from([node["name"] for node in nodes])
    G.add_nodes_from([node["id"] for node in nodes])
    for link in links:
        source = link["source"]
        target = link["target"]
        try:
            G.edges[source, target]["weight"] += 1
        except:
            G.add_edge(source, target, weight=1)

    for n in G:
        G.nodes[n]["name"] = n

    print(nx.info(G), "\n")

    return G


if __name__ == "__main__":
    import json
    import matplotlib.pyplot as plt
    # nodes: 189028 edges: 1046039
    # network = json.load(open("./test/Epinions.json"))
    # 37805 40701
    # network = json.load(open("./test/Epinions_20_percent.json"))
    # 18902 10418
    # network = json.load(open("./test/Epinions_10_percent.json"))
    # 2125 2831
    # network = json.load(open("./test/epinions_5_percent.json"))
    # 1889 109
    # network = json.load(open("./test/epinions_1_percent.json"))
    # network = json.load(open("./test/PolBooks.json"))
    # g = network_centrality(network)

    # network_centrality(network)
    from karateclub.dataset import GraphReader
    # print(GraphReader().get_features())
    g = GraphReader().get_graph()
    # print(GraphReader().get_target())
    # g = nx.newman_watts_strogatz_graph(1000, 20, 0.05)
    print(nx.info(g))
    print(g.nodes())

    # splitter = EgoNetSplitter(1.0)
    # splitter.fit(g)
    # print(splitter.get_memberships())

    # plt.show()
