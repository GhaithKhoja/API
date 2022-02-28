# TODO List API Build
## Introduction
This is a simple todo list built using Tornado as backend and React/HTML/CSS as frontend. The database was implemented using SQL.

## Setup Web Application

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

### Database

The application needs a localhost database that is hosted on a mysql server. The database needs to be intilized with a table of the following structure:

| Field  | Type | Null | Key | Default | Extra
| :---:  |:---: |:---: |:---:|:---:    | :---:  
| Name   |Varchar(20)|No|Pri|Null|
| Completed   |Varchar(3)|No||No|
| Creation   |timestamp|Yes||CURRENT_TIMESTAMP|DEFAULT_GENERATED
| LastEdit   |timestamp|Yes||CURRENT_TIMESTAMP|DEFAULT_GENERATED on update CURRENT_TIMESTAMP

The sql line used to create the table used in the API is the following:
```sql
create table list(
    Name varchar(20) not null primary key, 
    Completed varchar(3) not null DEFAULT 'No',
    Creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
    LastEdit TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    );
```

To connect to your database, put your database information in the main.py file located in the server file:
```python
# TO DO FILL THESE VALUES
root_username = 'TODO' # replace if you have a different root user name
user_password = 'TODO' # replace with your user's password
database_name = 'TODO' # the name you give to your database
table_name = 'TODO' # the name you give to your table
```

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