from Models.Food import Food
from Models.List import List
from Models.Goals import Goals
from Models.Donations import Donations
cnt = 0
class User(object):
    def __init__(self, id, name, password, idlist):
        self.id = id
        self.name = name
        self.password = password
        self.idlist = idlist

    def add_food(self, f):
        l = List(self.id, f)
        return l

    def add_goal(self, name):
        cnt =+1
        g = Goals(cnt, name, self.name)
        return g

    def add_donation(self, foodname, quantity, option):
        d = Donations(foodname, quantity, option, self.name)
        return d
