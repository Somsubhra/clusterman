# Headers
__author__ = 'somsubhra'


# The node class
class Node:

    # Constructor for the node class
    def __init__(self, server, username, password):
        self.server = server
        self.username = username
        self.password = password

    # String representation of node
    def to_string(self):
        return self.username + ":" + self.password + "@" + self.server