# Headers
__author__ = 'somsubhra'

# All imports
from nodes import Nodes
from multiclient import MultiClient


# The main Cluster Manager class
class ClusterMan:

    # Constructor for the Cluster Manager class
    def __init__(self, nodes_file):
        self.nodes = Nodes(nodes_file=nodes_file)
        self.multi_client = MultiClient(self.nodes)

    # Execute a command on all nodes
    def execute_command(self, command):
        self.multi_client.execute_command(command)
