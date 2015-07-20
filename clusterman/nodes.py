# Headers
__author__ = 'somsubhra'


# The nodes class
class Nodes:

    # Constructor for the nodes class
    def __init__(self, nodes_file):
        self.nodes_file_name = nodes_file

    def get_list(self):

        nodes_list = []

        try:
            nodes_file = open(self.nodes_file_name)

            for line in nodes_file.readlines():
                nodes_list.append(line.rstrip())

            nodes_file.close()
        except Exception as ex:
            print "Error opening nodes file \'" + self.nodes_file_name + "\'. " + ex.message
            exit()

        return nodes_list
