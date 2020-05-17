from BusinessLayer.User import check_account
from Commands.EventHandler import EventHandler
from DataAccess import DBConnectionUser, DBConnectionFood
from DataAccess.DBConnectionUser import insert_into_database
from Models.Food import Food
from Models.Goals import Goals
from Models.User import User
from DataAccess import  DBConneactionGoals


class Mediator_Commands():
    def __init__(self):
        pass

    def add_user(self, cnt, username, password):
        u = User(cnt, username, password, cnt)
        h = EventHandler()
        h.handle(DBConnectionUser.insert_into_database(u))

    def add_goal(self, cnt, goal, user):
        g = Goals(cnt, goal, user)
        h = EventHandler()
        h.handle(DBConneactionGoals.insert_into_database(g))

    def add_food(self, name, quantity, calories, expiredate):
        f = Food(name, quantity, calories, expiredate)
        f.observe("food to donate:", f.donate_op)
        m1 = Food.compute_calories_perday(f)
        m2 = Food.compute_grams_perday(f)
        h = EventHandler()
        h.handle(DBConnectionFood.insert_into_database(f))