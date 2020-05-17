from flask import Flask, render_template, redirect, url_for, request, session, abort, flash
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

from BusinessLayer.Food import validate_food
from BusinessLayer.Goals import validate_goal
from DataAccess import DBConnectionList
from DataAccess.DBConneactionGoals import insert_into_database
from Models import List
from Models.Food import Food
from Models.Goals import Goals
from Mediator.MediatorC import Mediator_Commands
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



def add_goal():
    msg = ''
    if session.get('loggedin') == True:
        if request.method == 'POST' and 'goal' in request.form :
            goal = request.form['goal']
            if validate_goal(goal) == 'ok':
                cnt =+ 1
                user = session['username']
                '''g = Goals(cnt, goal, user)
                insert_into_database(g)'''
                m = Mediator_Commands()
                m.add_goal(cnt, goal, user)
                flash(goal)
                return render_template('welcome.html', msg=msg)
    return render_template('addgoal.html', msg=msg)