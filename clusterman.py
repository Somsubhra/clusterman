#!/usr/bin/env python
__author__ = 'somsubhra'

# All imports
import sys
from clusterman import ClusterMan
from clusterman import CMParser

# The main method
def main():
    if len(sys.argv) > 2:
        nodes_file = sys.argv[1]
        cm_file = sys.argv[2]
    else:
        print "Usage: clusterman.py <nodes_file> <cm_file>"
        exit()

    cluster_manager = ClusterMan(nodes_file=nodes_file)
    cm_parser = CMParser(cm_file, cluster_manager)
    cm_parser.parse()

# Invocation of the main method
if __name__ == "__main__":
    main()
