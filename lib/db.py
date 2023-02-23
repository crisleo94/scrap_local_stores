import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    port="33060",
    user="root",
    password="admin1234",
)

cursor = mydb.cursor()

cursor.execute("USE store_data")