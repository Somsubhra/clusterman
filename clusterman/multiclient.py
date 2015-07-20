# Headers
__author__ = 'somsubhra'

# All imports
from paramiko import SSHClient
from nodes import Nodes
from node import Node


# The Multi-Client class
class MultiClient:

    # Constructor for the multi-client class
    def __init__(self, nodes):
        self.nodes = nodes.get_list()

        self.ssh_clients = []

        for node in self.nodes:
            ssh_client = SSHClient()
            ssh_client.load_system_host_keys()
            ssh_client.connect(node.server, username=node.username, password=node.password)