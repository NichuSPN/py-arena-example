from arena.data import Postgres, SQLite, MySQL

# Callback functions for after we run the query
def onSuccess(result):
    print("Query Ran successfully")
    return True, result

def onError(error):
    print("Error while running a query ", error)
    raise Exception("Error running a query", error)

# Add correct credentials to connect to Postgres instance you want to work with...
pg = Postgres({
    "host": "localhost", 
    "user": "username", 
    "password": "password",
    "port": 5432,
    "database": "database"})

# Create a table
pg.run_query("create table arena_test (name text);", 
                             isUpdate=True, 
                             onSuccess=onSuccess,
                             onError=onError)

# Insert a few elements
pg.run_query("insert into arena_test (name) values ('Hello'), ('World'), ('Test');", 
             isUpdate=True, 
             onSuccess=onSuccess,
             onError=onError)

# Select after substituting the value in the templatized query
success, result = pg.run_query("select * from arena_test where name='{{name}}'",
                               params = {"name": "Hello"})
if success:
    print("Here is the result", result)
else:
    print("Error occured", result)
    
# Drop the table
pg.run_query("drop table arena_test;", 
             isUpdate=True, 
             onSuccess=onSuccess,
             onError=onError)

# Close the created connection
pg.close_connection()

# Connect to the sqlite DB
sqlite = SQLite("py-arena-test.db")

# Create a table
sqlite.run_query("create table arena_test (name text);", 
                 isUpdate=True, 
                 onSuccess=onSuccess,
                 onError=onError)

# Insert a few elements
sqlite.run_query("insert into arena_test (name) values ('Hello'), ('World'), ('Test');", 
                 isUpdate=True, 
                 onSuccess=onSuccess,
                 onError=onError)

# Select after substituting the value in the templatized query
success, result = sqlite.run_query("select * from arena_test where name='{{name}}'",
                               params = {"name": "Hello"})
if success:
    print("Here is the result", result)
else:
    print("Error occured", result)
    
# Drop the table
sqlite.run_query("drop table arena_test;", 
                 isUpdate=True, 
                 onSuccess=onSuccess,
                 onError=onError)

# Close the created connection
sqlite.close_connection()

# Connect to your MySQL database
mysql = MySQL({"host": "localhost",
               "user": "username",
               "password": "password",
               "database": "db",
               "port": 3306})

# Create a table
mysql.run_query("create table arena_test (name text);", 
                 isUpdate=True, 
                 onSuccess=onSuccess,
                 onError=onError)

# Insert a few elements
mysql.run_query("insert into arena_test (name) values ('Hello'), ('World'), ('Test');", 
                 isUpdate=True, 
                 onSuccess=onSuccess,
                 onError=onError)

# Select after substituting the value in the templatized query
success, result = mysql.run_query("select * from arena_test where name='{{name}}'",
                               params = {"name": "Hello"})
if success:
    print("Here is the result", result)
else:
    print("Error occured", result)
    
# Drop the table
mysql.run_query("drop table arena_test;", 
                 isUpdate=True, 
                 onSuccess=onSuccess,
                 onError=onError)

# Close the created connection
mysql.close_connection()


