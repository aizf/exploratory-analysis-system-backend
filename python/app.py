from flask import Flask, request
from flask_cors import CORS
from lib import Frequent_item, cluster, network_centrality, communities, save
import json
app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def index():
    return "Hello"


@app.route('/frequent_item', methods=['POST'])
def frequent_item():
    data = request.json
    # print(data)
    group = Frequent_item.gen_group_X([d['operation'] for d in data])
    res = Frequent_item.calc(group)
    return {'data': res}


@app.route('/cluster', methods=['POST'])
def cluster_route():
    data = request.json
    # print(data["algorithm"], data["params"])
    nodes = data["nodes"]
    pred = cluster(data["algorithm"], nodes, data.get("params", {}))
    # print(pred)
    res = []
    for (i, node) in enumerate(nodes):
        # print("node", node)
        # print("pred", pred)
        res.append({"uid": node["uid"], "group": int(pred[i])})
    print(res[:5], "......")
    return {'data': res}


@app.route('/network_centrality', methods=['POST'])
def network_centrality_route():
    network = request.json
    # print(data["algorithm"], data["params"])
    res, g = network_centrality(network)
    # print(res[:5], "......")
    return {'data': res}


@app.route('/communities', methods=['POST'])
def communities_route():
    network = request.json
    # print(data["algorithm"], data["params"])
    res, g = communities(network)
    # print(res[:5], "......")
    return {'data': res}


@app.route('/save', methods=['POST'])
def save_route():
    network = request.json
    # print(data["algorithm"], data["params"])
    res = save(network)
    # print(res[:5], "......")
    return {'data': res}


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)