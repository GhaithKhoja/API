# TODO List Build
## Introduction
This is a simple todo list built using Tornado as backend and react/html/css as frontend. The database was implemented using SQL.

## Setup Web Application
### Create and Start

Set current directory to server folder, which contains main.py.
Install the requirments from requirements.txt, Then run:

```bash
python3 main.py
```

Which will create and create and and start the containers defined in the multi-container compose file.

### Connect

Connect to the application in host computer by typing `http://localhost:8881` into a browser.

### Usage
The valid commands in the web application are:
```
add
delete
check
uncheck
```
Commands and entrys to the list can be submitted using the form box