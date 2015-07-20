#!/usr/bin/env python
__author__ = 'somsubhra'

# All imports
import sys
from clusterman import ClusterMan


# The main method
def main():
    if len(sys.argv) > 1:
        nodes_file = sys.argv[1]
    else:
        nodes_file = "nodes"

    cluster_manager = ClusterMan(nodes_file=nodes_file)

# Invocation of the main method
if __name__ == "__main__":
    main()
