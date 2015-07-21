# Headers
__author__ = 'somsubhra'

# All imports
from flask import Flask, render_template

# All constant definitions
HOST = "127.0.0.1"
PORT = 5000
DEBUG = True

# Create an instance of the webapp
app = Flask(__name__)


# The index page route
@app.route('/')
def index_handler():
    return render_template("index.html")

# Run the app
app.run(host=HOST, port=PORT, debug=DEBUG)
