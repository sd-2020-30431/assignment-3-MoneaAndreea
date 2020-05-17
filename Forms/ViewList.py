from flask import Flask, render_template, redirect, url_for, request, session, abort, flash
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

from BusinessLayer.User import check_account
from DataAccess.DBConnectionUser import insert_into_database
from Models.User import User
from Mediator.MediatorQ import Mediator_Query
global cnt
cnt = 0
app = Flask(__name__)
app.secret_key = 'watermelonsugar'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'wasteless'

# Intialize MySQL
mysql = MySQL(app)

def show_item():
    try:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        m = Mediator_Query()
        data = m.view_list()
        print(data)
        return render_template("showitem.html", data=data)
    except Exception as e:
        return str(e)