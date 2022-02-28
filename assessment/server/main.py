import tornado.web
import tornado.ioloop
import pymysql

class SPA(tornado.web.RequestHandler):
    def get(self):

        # Connection to mysql database on my localhost and init cursor
        db = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='ghaith', # replace if you have a different root user name
            password='12345678', # replace with your user's password
            db='todo' # the name you give to your database
        )
        cursor = db.cursor()

        #Select all the current data in the database and display it
        cursor.execute("SELECT * FROM list;")
        data = cursor.fetchall()
        items = data

        #Message to display in the page
        msg = 'Enter a command!'

        #Render the HTML
        self.render("index.html", items=items, msg=msg)

    def post(self):

        #Fetch arguments from the form
        command = self.get_argument('command')
        name = self.get_argument('name')

        # Connection to mysql database on my localhost and init cursor
        db = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='ghaith', # replace if you have a different root user name
            password='12345678', # replace with your user's password
            db='todo' # the name you give to your database
        )
        cursor = db.cursor()

        #Message to display
        msg = 'Enter a command!'

        #To Do Proccess if command and task are valid then act on the command 
        if command and name:
            
            #Turn inputs into strings and lowercase them
            command, name = str(command).lower(), str(name).lower()

            #Add an entry to the list
            if command == "add":
                try:
                    cursor.execute(f"INSERT INTO list(Name) values ('{name}');")
                except Exception as e:
                    msg = e
                    print(e)

            #Remove an entry from the list
            elif command == "delete":
                try:
                    cursor.execute(f"DELETE FROM list where Name='{name}';")
                except Exception as e:
                    msg = e
                    print(e)
            
            #Mark an entry as complete
            elif command == "check":
                try:
                    cursor.execute(f"UPDATE list SET Completed='Yes' WHERE Name='{name}';")
                except Exception as e:
                    msg = e
                    print(e)

            #Mark an entry as incomplete
            elif command == "uncheck":
                try:
                    cursor.execute(f"UPDATE list SET Completed='No' WHERE Name='{name}';")
                except Exception as e:
                    msg = e
                    print(e)

            #If command is unknown
            else:
                msg = "Command Unknown"

        #Commit changes to the database and select the data to display them
        db.commit()
        cursor.execute("SELECT * FROM list;")
        data = cursor.fetchall()
        items = data

        #HTML rendering with the variables 
        self.render("index.html", items=items, msg=msg)

#Path for files such as React or CSS
settings = {
    "static_path": "static"
}

if __name__ == "__main__":

    #Run App
    app = tornado.web.Application([
        (r"/", SPA),
    ], **settings, debug=True)

    app.listen(8881)
    tornado.ioloop.IOLoop.current().start()