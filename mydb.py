import mysql.connector

database = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='mysecurepassword'
)

cursor = database.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS crm")

print("All done!")
