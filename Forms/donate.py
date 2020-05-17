from flask import Flask, render_template, redirect, url_for, request, session, abort, flash
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

from BusinessLayer.Donations import validate_donation
from BusinessLayer.Food import validate_food
from DataAccess import DBConnectionList
from DataAccess.BDConnectionDonations import insert_into_database
from Models import List
from Models.Donations import Donations
from Models.Food import Food

app = Flask(__name__)
app.secret_key = 'watermelonsugar'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'wasteless'

# Intialize MySQL
mysql = MySQL(app)
global cnt
cnt = 0
def donate_():
    msg = ''
    if session.get('loggedin') == True:
        if request.method == 'POST' and 'name' in request.form and 'quantity' in request.form  and 'option' in request.form:
            name = request.form['name']
            quantity = request.form['quantity']
            option = request.form['option']
            if validate_donation(name, quantity):
                user = session['username']
                d = Donations(name, quantity, option, user)
                insert_into_database(d)
                return render_template('welcome.html', msg=msg)
    return render_template('donate.html', msg=msg)