# Headers
__author__ = 'somsubhra'

# All imports
from node import Node


# The nodes class
class Nodes:

    # Constructor for the nodes class
    def __init__(self, nodes_file):
        self.nodes_file_name = nodes_file

        self.nodes_list = []

        try:
            nodes_file_obj = open(self.nodes_file_name)

            for line in nodes_file_obj.readlines():
                items = line.rstrip().split()
                self.nodes_list.append(Node(server=items[0], username=items[1], password=items[2]))

            nodes_file_obj.close()
        except Exception as ex:
            print "Error opening nodes file \'" + self.nodes_file_name + "\'. " + ex.message
            exit()

    # Get the list of nodes
    def get_list(self):
        return self.nodes_list

    # String representation of nodes
    def to_string(self):
        output = ""
        for node in self.nodes_list:
            output += node.to_string() + "\n"

        return output
