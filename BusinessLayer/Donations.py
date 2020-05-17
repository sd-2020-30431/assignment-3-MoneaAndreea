import re
from flask import Flask, render_template, redirect, url_for, request, session, abort, flash
from flask_mysqldb import MySQL
import MySQLdb.cursors
app = Flask(__name__)
app.secret_key = 'watermelonsugar'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'wasteless'

# Intialize MySQL
mysql = MySQL(app)


def validate_donation(foodname, quantity):
    if  not re.match(r'[A-Za-z]+', foodname):
        msg = "Food name must contain only letters"
        return msg
    elif not re.match(r'[0-9]+', quantity):
        msg = "Quantity must contain only numbers"
        return msg
    else:
        msg = "ok"
        return msg
