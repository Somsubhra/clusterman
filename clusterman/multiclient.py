# Headers
__author__ = 'somsubhra'

# All imports
import paramiko
from nodes import Nodes
from node import Node


# The Multi-Client class
class MultiClient:

    # Constructor for the multi-client class
    def __init__(self, nodes):
        self.nodes = nodes.get_list()

        self.ssh_clients = {}

        paramiko.util.log_to_file("ssh.log")

        for node in self.nodes:
            ssh_client = paramiko.SSHClient()
            ssh_client.load_system_host_keys()
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh_client.connect(node.server, username=node.username, password=node.password)

            self.ssh_clients[node] = ssh_client

    # Execute a command on all nodes
    def execute_command(self, command):
        for node in self.ssh_clients:
            stdin, stdout, stderr = self.ssh_clients[node].exec_command(command)

            print "Node: " + node.server + " Command: " + command

            output = ""

            for line in stdout.readlines():
                output += line

            for line in stderr.readlines():
                output += line

            print output