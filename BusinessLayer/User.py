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
def check_account(username, password):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
    account = cursor.fetchone()
    # If account exists show error and validation checks
    if account:
        msg = 'Account already exists!'
        return msg
    elif not re.match(r'[A-Za-z0-9]+', username):
        msg = 'Username must contain only characters and numbers!'
        return msg
    elif not username or not password:
        msg = 'Please fill out the form!'
        return msg
    else:
        msg ="ok"
        return msg