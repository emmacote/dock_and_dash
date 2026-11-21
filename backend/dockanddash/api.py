from flask import Flask, jsonify, request
from flask_cors import CORS
from . import client

app = Flask(__name__)

CORS(app)

@app.route("/activecontainers")
def get_containers():
    string_keys = [
        'AppArmorProfile', 'Created',
        'Driver',          'HostnamePath',
        'HostsPath',       'Id',
        'Image',           'LogPath',
        'MountLabel',      'Name',
        'Path',            'Platform',
        'ProcessLabel',    'ResolvConfPath'
    ]
    json_list = []
    for container in client.containers.list():
        new_ob = dict()
        for string_key in string_keys:
            new_ob[string_key] = container.attrs[string_key]
        json_list.append(new_ob)

    return jsonify({"containers": json_list})


@app.route("/inactivecontainers")
def get_inactive_containers():
    string_keys = [
        'AppArmorProfile', 'Created',
        'Driver',          'HostnamePath',
        'HostsPath',       'Id',
        'Image',           'LogPath',
        'MountLabel',      'Name',
        'Path',            'Platform',
        'ProcessLabel',    'ResolvConfPath'
    ]

    containers = client.containers.list(filters=dict(status="exited"))

    json_list = []
    for container in containers:
        new_ob = dict()
        for string_key in string_keys:
            new_ob[string_key] = container.attrs[string_key]
        json_list.append(new_ob)

    return jsonify({"containers": json_list})

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
    string_keys = ['Created', 'Driver', 'Id', 'Name', 'Scope']

    json_list = []
    for network in client.networks.list():
        new_ob = dict()
        for string_key in string_keys:
            new_ob[string_key] = network.attrs[string_key]
        json_list.append(new_ob)

    return jsonify({"networks": json_list})

