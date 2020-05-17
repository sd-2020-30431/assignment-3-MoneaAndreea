import mysql.connector

from Models.Donations import Donations

mydb=mysql.connector.connect(host="localhost", user="root", password="root", database = "wasteless")

mycursor = mydb.cursor()

def insert_into_database(d):
    try:
        sql_query = "INSERT INTO donation (foodname, quantity, option, user) VALUES (%s, %s, %s, %s)"
        record_tuple = (d.foodname, d.quantity, d.option, d.user)
        mycursor.execute(sql_query, record_tuple)
        mydb.commit()
    except mysql.connector.Error as error:
        print("Failed to insert record ")

def update_into_database(d):
    try:
        sql_query = "Update donation set to = %s where foodname = %s"
        record_tuple = (d.to, d.foodname)
        mycursor.execute(sql_query, record_tuple)
        mydb.commit()
    except mysql.connector.Error as error:
        print("Failed to update record ")

def delete_from_database(d):
    try:
        sql_query = "Delete from food where name = %s"
        mycursor.execute(sql_query, (d.foodname,))
        mydb.commit()
    except mysql.connector.Error as error:
        print("Failed to delete record ")

