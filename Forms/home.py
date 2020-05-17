from flask import Flask, render_template, redirect, url_for, request, session, abort, flash
from flask_mysqldb import MySQL

import MySQLdb.cursors
import re


app = Flask(__name__)
app.secret_key = 'watermelonsugar'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'wasteless'

# Intialize MySQL
mysql = MySQL(app)


def home_():
    # Check if user is loggedin
    if 'loggedin' in session:
        # User is loggedin show them the home page
        return render_template('welcome.html', username=session['username'])
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))