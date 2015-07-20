clusterman
========

Web based (plus command line) utility to manage a cluster

# Running from command line

### Adding a nodes file
* Add a <file_name>.nodes file containing nodes data in following format:
```
<server> <username> <password>
```

### Adding a cm file
* A <file_name>.cm file contains commands to be executed across the cluster.
* Add a <file_name>.cm file with a single command on each line.

### Get it running
* Execute the following command to execute the commands across the cluster:
```
clusterman.py <nodes_file> <cm_file>
```