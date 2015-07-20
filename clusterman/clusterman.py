# Headers
__author__ = 'somsubhra'

# All imports
from nodes import Nodes


# The main Cluster Manager class
class ClusterMan:

    # Constructor for the Cluster Manager class
    def __init__(self, nodes_file):
        self.nodes = Nodes(nodes_file=nodes_file)
        nodes_list = self.nodes.get_list()
        print(nodes_list)
