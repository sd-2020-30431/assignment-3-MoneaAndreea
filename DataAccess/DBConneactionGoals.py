import mysql.connector
mydb=mysql.connector.connect(host="localhost", user="root", password="root", database = "wasteless")

mycursor = mydb.cursor()

def insert_into_database(g):
    try:
        sql_query = "INSERT INTO goal (idgoal, name, user) VALUES (%s, %s, %s)"
        record_tuple = (g.idgoal, g.name, g.user)
        mycursor.execute(sql_query, record_tuple)
        mydb.commit()
    except mysql.connector.Error as error:
        print("Failed to insert record ")

def update_into_database(g):
    try:
        sql_query = "Update goal set name = %s where iduser = %s"
        record_tuple = (g.name, g.iduser)
        mycursor.execute(sql_query, record_tuple)
        mydb.commit()
    except mysql.connector.Error as error:
        print("Failed to update record ")

def delete_from_database(g):
    try:
        sql_query = "Delete from goal where name = %s"
        mycursor.execute(sql_query, (g.name,))
        mydb.commit()
    except mysql.connector.Error as error:
        print("Failed to delete record ")
