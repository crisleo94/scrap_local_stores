import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    port="33060",
    user="root",
    password="admin1234",
)

cursor = mydb.cursor()

cursor.execute("USE store_data")

# queries
def insert_into_table(table_name, params):
    sql_insert = ""
    if table_name == 'olimpica' or table_name == 'exito':
        sql_insert = f"INSERT INTO {table_name} (name, price, valid_until) VALUES (%s, %s, %s)"
    cursor.execute(sql_insert, params)
    mydb.commit()