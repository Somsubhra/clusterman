clusterman
========

Web based (plus command line) utility to manage a cluster.

# Setup
* Run the following command:
```
./setup.sh
```

# Running from command line

### Adding a nodes file
* Add a ```<file_name>.nodes``` file containing nodes data in following format on each line:
```
<server> <username> <password>
```

### Adding a cm file
* A ```<file_name>.cm``` file contains commands to be executed across the cluster.
* Add a ```<file_name>.cm``` file with a single command on each line.

### Get it running
* Execute the following command to execute the commands across the cluster:
```
clusterman.py <nodes_file> <cm_file>
```

# Running the web console
### Adding a nodes file
* Add a ```default.nodes``` file containing node data as specified above.

### Get it running
* Execute the following command to run the web console:
```
./clusterweb.py
```
* Access the web console at http://localhost:8000
