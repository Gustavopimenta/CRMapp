import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '' 
)

cursorObject = dataBase.cursor()

#create a database
cursorObject.execute("CREATE DATABASE elderco1")

print('All done!')