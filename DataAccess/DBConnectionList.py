import mysql.connector
mydb=mysql.connector.connect(host="localhost", user="root", password="root", database = "wasteless")

mycursor = mydb.cursor()

def insert_into_database(l):
    try:
        sql_query = "INSERT INTO foodlist (idfoodlist, foodname) VALUES (%s, %s)"
        record_tuple = (l.id, l.name)
        mycursor.execute(sql_query, record_tuple)
        mydb.commit()
    except mysql.connector.Error as error:
        print("Failed to insert record ")

def update_into_database(l):
    try:
        sql_query = "Update foodlist set name = %s where idfoodlist = %s"
        record_tuple = (l.name, l.id)
        mycursor.execute(sql_query, record_tuple)
        mydb.commit()
    except mysql.connector.Error as error:
        print("Failed to update record ")

def delete_from_database(l):
    try:
        sql_query = "Delete from foodlist where name = %s"
        mycursor.execute(sql_query, (l.name,))
        mydb.commit()
    except mysql.connector.Error as error:
        print("Failed to delete record ")
