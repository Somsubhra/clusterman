__author__ = 'somsubhra'

from clusterman import ClusterMan

# The CM File Parser
class CMParser:

    # Constructor for the CM File parser
    def __init__(self, cm_file, cluster_manager):
        self.cm_file = cm_file
        self.cluster_manager = cluster_manager

    # Parse and execute file
    def parse(self):

        try:
            cm_file_obj = open(self.cm_file)

            for command in cm_file_obj.readlines():
                self.cluster_manager.execute_command(command.rstrip())

            cm_file_obj.close()
        except Exception as ex:
            print "Error executing .cm file \'" + self.cm_file + "\' " + ex.message