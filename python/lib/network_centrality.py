import networkx as nx


def network_centrality(network):
    nodes = network["nodes"]
    links = network["links"]
    G = nx.Graph()
    G.add_nodes_from([node["id"] for node in nodes])
    G.add_edges_from([(link["source"], link["target"]) for link in links])
    for n in G:
        G.nodes[n]["name"] = n
    # d = nx.readwrite.json_graph.node_link_data(G)
    # json.dump(d, open("./temp.json", "w"))
    # for n in G:
    #     print(type(n))
    # print(nx)
    # print(nx.info(G), "\n")
    # print("density", nx.density(G), "\n")
    # print("degree", nx.degree(G), "\n")
    data = {
        "density":
        nx.density(G),
        "column": [
            "degree_centrality", "closeness_centrality",
            "betweenness_centrality", "eigenvector_centrality", "pagerank"
        ],
        "row": [],
        "data": []
    }
    degree_centrality = nx.degree_centrality(G)
    closeness_centrality = nx.closeness_centrality(G)
    betweenness_centrality = nx.betweenness_centrality(G)
    eigenvector_centrality = nx.eigenvector_centrality(G)
    pagerank = nx.pagerank(G)

    for n in G:
        data["row"].append(n)
        data["data"].append([
            degree_centrality[n], closeness_centrality[n],
            betweenness_centrality[n], eigenvector_centrality[n], pagerank[n]
        ])
    return data


if __name__ == "__main__":
    import json
    import matplotlib.pyplot as plt
    network = json.load(open("./test/miserables.json"))
    data = network_centrality(network)
    print(data)

    # plt.figure(figsize=(12, 12))
    # plt.subplot(111)
    # nx.draw(G, with_labels=True)
    # plt.show()