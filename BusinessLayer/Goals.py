import re
from flask import Flask, render_template, redirect, url_for, request, session, abort, flash
from flask_mysqldb import MySQL
import MySQLdb.cursors


# Intialize MySQL


def validate_goal(name):
    if  not re.match(r'[A-Za-z0-9]+', name):
        msg = "Goal must contain only letters or numbers"
        return msg
    else:
        msg = "ok"
        return msg
