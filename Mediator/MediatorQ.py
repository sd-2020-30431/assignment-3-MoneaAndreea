import MySQLdb
from flask import Flask
from flask_mysqldb import MySQL

from BusinessLayer.User import check_account
from Commands.EventHandler import EventHandler
from DataAccess.DBConnectionUser import insert_into_database
from Models.Food import Food
from Models.Goals import Goals
from Models.User import User
from Queries.MessageHandler import MessageHandler

app = Flask(__name__)
app.secret_key = 'watermelonsugar'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'wasteless'
mysql = MySQL(app)

class Mediator_Query():
    def __init__(self):
        pass

    def view_list(self):
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        h = MessageHandler()
        h.handle(cursor.execute("SELECT name, quantity, calories, expiredate from food"))
        data = h.handle(cursor.fetchall())
        return data