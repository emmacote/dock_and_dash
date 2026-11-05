from flask import Flask, jsonify, request
from flask_cors import CORS
from . import client



app = Flask(__name__)

CORS(app)

@app.route("/activecontainers")
def get_containers():
    containers = [ c.name for c in client.containers.list()]
    return jsonify(dict(containers=containers))


@app.route("/inactivecontainers")
def get_inactive_containers():
    containers = client.containers.list(filters=dict(status="exited"))
    containers = [c.name for c in containers]
    return jsonify(dict(containers=containers))


@app.route("/volumes")
def get_volumes():
    volumes = [v.name for v in client.volumes.list()]
    return jsonify(dict(volumes=volumes))


@app.route("/images")
def get_images():
    json_list = [dict(id=image.id, tags=[tag for tag in image.tags]) for image in client.images.list()]
    json_list = []
    for image in client.images.list():
        image_info = dict(id=image.id, tags=image.tags)
        json_list.append(image_info)
    return jsonify({"images": json_list})


@app.route("/logs/<container_name>")
def get_logs(container_name):
    container = client.containers.get(container_name)
    print(container.logs())
    container.logs().decode().split("\n")
    return jsonify(dict(logs=container.logs().decode().split("\n")))


@app.route("/networks")
def get_networks():
    network_list = []

    for network in client.networks.list(greedy=True):
        network_info = dict(id=network.id, name=network.name, short_id=network.short_id)

        for container in network.containers:
            print(container.name)

        network_containers = [container.name for container in network.containers]
        network_info["containers"] = network_containers
        network_list.append(network_info)

    return jsonify(dict(networks=network_list))

