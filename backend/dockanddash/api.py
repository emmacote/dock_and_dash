from flask import Flask, jsonify, request
from flask_cors import CORS
from . import client

app = Flask(__name__)

CORS(app)

@app.route("/activecontainers")
def get_containers():
    containers = [ c.attrs for c in client.containers.list()]
    return jsonify(dict(containers=containers))


@app.route("/inactivecontainers")
def get_inactive_containers():
    containers = client.containers.list(filters=dict(status="exited"))
    containers = [c.attrs for c in containers]
    return jsonify(dict(containers=containers))


@app.route("/volumes")
def get_volumes():
    volumes = [v.attrs for v in client.volumes.list()]
    return jsonify(dict(volumes=volumes))


@app.route("/images")
def get_images():
    string_keys = [ 'Architecture', 'Comment', 'Created', 'Id', 'Os' ]

    json_list = []
    for image in client.images.list():
        new_ob = dict()
        for string_key in string_keys:
            new_ob[string_key] = image.attrs[string_key]
        json_list.append(new_ob)

    return jsonify({"images": json_list})


@app.route("/logs/<container_name>")
def get_logs(container_name):
    container = client.containers.get(container_name)
    print(container.logs())
    container.logs().decode().split("\n")
    return jsonify(dict(logs=container.logs().decode().split("\n")))


@app.route("/networks")
def get_networks():
    network_list = [network.attrs for network in client.networks.list()]
    return jsonify(dict(networks=network_list))

