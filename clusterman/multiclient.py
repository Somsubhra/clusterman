# Headers
__author__ = 'somsubhra'

# All imports
from paramiko import SSHClient


# The Multi-Client class
class MultiClient:

    # Constructor for the multi-client class
    def __init__(self, nodes_list, username, password):
        self.nodes_list = nodes_list
        self.username = username
        self.password = password
