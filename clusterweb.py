#!/usr/bin/env python

# Headers
__author__ = 'somsubhra'

# All imports
from flask import Flask, render_template, request, jsonify
from clusterman import ClusterMan

# All constant definitions
HOST = "127.0.0.1"
PORT = 5000
DEBUG = True

# Create an instance of the webapp
app = Flask(__name__)
cluster_manager = ClusterMan(nodes_file="default.nodes")


# The index page route
@app.route('/')
def index_handler():
    return render_template("index.html")


@app.route('/api')
def api_handler():
    output = cluster_manager.execute_command(request.args.get("command"))

    json_result = {
        "output": output
    }

    return jsonify(**json_result)

# Run the app
app.run(host=HOST, port=PORT, debug=DEBUG)
