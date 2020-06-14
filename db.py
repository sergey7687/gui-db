import mysql.connector
# connection to mysql DB
my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=" ",
    database='mydb'
)


