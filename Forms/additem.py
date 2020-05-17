from flask import Flask, render_template, redirect, url_for, request, session, abort, flash
from flask_mysqldb import MySQL

from BusinessLayer.Food import validate_food
from DataAccess.DBConnectionFood import insert_into_database
from Models import List
from Models.Food import Food, Event
import Models.User
from Mediator.MediatorC import Mediator_Commands
app = Flask(__name__)
app.secret_key = 'watermelonsugar'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'wasteless'

# Intialize MySQL
mysql = MySQL(app)


def add_item():
    msg = ''
    if request.method == 'POST' and 'name' in request.form and 'quantity' in request.form and 'calories' in request.form and 'expiredate' in request.form:
        name = request.form['name']
        quantity = request.form['quantity']
        calories = request.form['calories']
        expiredate = request.form['expiredate']
        if validate_food(name, quantity, calories, expiredate) == 'ok':
            m = Mediator_Commands()
            m.add_food(name, quantity, calories, expiredate)
            return render_template('welcome.html', msg=None)
    return render_template('additem.html', msg=None)
