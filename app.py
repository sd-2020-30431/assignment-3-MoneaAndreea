from flask import Flask, render_template, redirect, url_for, request, session, abort, flash
from flask_mysqldb import MySQL
import MySQLdb.cursors

from Forms.ViewList import show_item
from Forms.addgoal import add_goal
from Forms.additem import add_item
from Forms.home import home_
from Forms.login import log_in
from Forms.logout import log_out
from Forms.register import register_
from Forms.donate import donate_


app = Flask(__name__)
app.secret_key = 'watermelonsugar'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'wasteless'

# Intialize MySQL
mysql = MySQL(app)

@app.route('/')
def home():
    return home_()

@app.route('/login', methods=['GET', 'POST'])
def login():
   return log_in()

@app.route('/register', methods=['GET', 'POST'])
def register():
    return register_()

@app.route('/logout' )
def logout():
    return log_out()

@app.route('/additem',  methods=['GET', 'POST'])
def additem():
    return add_item()


@app.route('/addgoal',  methods=['GET', 'POST'])
def addgoal():
    return add_goal()

@app.route('/donate', methods=['GET', 'POST'])
def doantefood():
        return donate_()


@app.route('/showitem', methods =['GET'])
def showitem():
    return show_item()

if __name__ == '__main__':
    app.run(debug=True)