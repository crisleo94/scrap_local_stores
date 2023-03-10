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
    cursor.execute(f"SHOW TABLES LIKE '{table_name}'")
    found_table = cursor.fetchone()

    if found_table:
        cursor.execute(f"DROP TABLE {table_name}")

    create_table = f"""
        CREATE TABLE {table_name} (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            price FLOAT NOT NULL,
            valid_until VARCHAR(255) NOT NULL,
            category VARCHAR(255) NOT NULL
        )
    """
    cursor.execute(create_table)

    sql_insert = f"INSERT INTO {table_name} (name, price, valid_until, category) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql_insert, params)

    mydb.commit()

def get_data(table_name, category, limit):
    sql_result = f"SELECT * FROM {table_name} WHERE category = %s LIMIT = %s"
    values = (category, limit)
    cursor.execute(sql_result, values)
    result = cursor.fetchall()
    mydb.commit()
    cursor.close()
    mydb.close()
    return result

def get_data_test():
    cursor.execute("SELECT * FROM olimpica")
    result = cursor.fetchall()
    return result