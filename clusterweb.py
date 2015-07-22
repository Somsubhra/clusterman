#!/usr/bin/env python

# Headers
__author__ = 'somsubhra'

# All imports
from flask import Flask, render_template, request, jsonify
from clusterman import ClusterMan

# All constant definitions
HOST = "0.0.0.0"
PORT = 8000
DEBUG = False

# Create an instance of the webapp
app = Flask(__name__)
cluster_manager = ClusterMan(nodes_file="default.nodes")


# The index page route
@app.route('/')
def index_handler():
    connected_nodes = cluster_manager.nodes.to_string()
    return render_template("index.html", connected_nodes=connected_nodes)


# The API route
@app.route('/api')
def api_handler():
    output = cluster_manager.execute_command(request.args.get("command"))

    json_result = {
        "output": output
    }

    return jsonify(**json_result)

# Run the app
app.run(host=HOST, port=PORT, debug=DEBUG)
