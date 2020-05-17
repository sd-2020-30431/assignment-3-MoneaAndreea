import mysql.connector
mydb=mysql.connector.connect(host="localhost", user="root", password="root", database = "wasteless")

mycursor = mydb.cursor()

def insert_into_database(f):
    try:
        sql_query = "INSERT INTO food (name, quantity, calories, expiredate) VALUES (%s, %s, %s, %s)"
        record_tuple = (f.name, f.quantity, f.calories, f.expiredate)
        mycursor.execute(sql_query, record_tuple)
        mydb.commit()
    except mysql.connector.Error as error:
        print("Failed to insert record ")

def update_into_database(f):
    try:
        sql_query = "Update food set calories = %s where name = %s"
        record_tuple = (f.calories, f.name)
        mycursor.execute(sql_query, record_tuple)
        mydb.commit()
    except mysql.connector.Error as error:
        print("Failed to update record ")

def delete_from_database(f):
    try:
        sql_query = "Delete from food where name = %s"
        mycursor.execute(sql_query, (f.name,))
        mydb.commit()
    except mysql.connector.Error as error:
        print("Failed to delete record ")
