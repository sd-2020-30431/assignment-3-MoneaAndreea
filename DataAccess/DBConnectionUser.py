import mysql.connector
import Models.User
mydb=mysql.connector.connect(host="localhost", user="root", password="root", database = "wasteless")

mycursor = mydb.cursor()

def insert_into_database(u):
    try:
        sql_query = "INSERT INTO users (iduser, username, password, foodlistid) VALUES (%s, %s, %s, %s)"
        record_tuple = (u.id, u.name, u.password, u.idlist)
        mycursor.execute(sql_query, record_tuple)
        mydb.commit()
    except mysql.connector.Error as error:
        print("Failed to insert record ")

def update_into_database(u):
    try:
        sql_query = "Update users set username = %s where iduser = %s"
        record_tuple = (u.name, u.id)
        mycursor.execute(sql_query, record_tuple)
        mydb.commit()
    except mysql.connector.Error as error:
        print("Failed to update record ")

def select_user(username):
    try:
        sql_query = "SELECT  id, username, password, idlist from users where username = %s"
        record_tuple = (username)
        mycursor.execute(sql_query, record_tuple)
        data = mycursor.fetchall()
        return data
    except mysql.connector.Error as error:
        print("Failed to update record ")

def delete_from_database(u):
    try:
        sql_query = "Delete from users where username = %s"
        mycursor.execute(sql_query, (u.name,))
        mydb.commit()
    except mysql.connector.Error as error:
        print("Failed to delete record ")
