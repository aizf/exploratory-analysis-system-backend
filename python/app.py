from flask import Flask, request
from flask_cors import CORS
from lib import Frequent_item, cluster
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
    for ( i,node) in enumerate(nodes):
        # print("node", node)
        # print("pred", pred)
        res.append({"uid": node["uid"], "group": int(pred[i])})
    print(res)
    return {'data': res}


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)