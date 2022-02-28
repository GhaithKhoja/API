# TODO List Build
## Introduction
This is a simple todo list built using Tornado as backend and React/HTML/CSS as frontend. The database was implemented using SQL.

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
To use commands with their entries, use the text box on the top of the web application.
To gain more understanding about the functions of the commands and how to use them, Click the "help" button in the web application.

### Structure
The projects structure is as follows
```
assessment/
    Server/ 
        Static/
            Css/
            JS/
```

The server folder contains the main python driver and the index html.
The static folder contains the CSS and JS used for React.
