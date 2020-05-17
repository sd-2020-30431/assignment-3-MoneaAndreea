from flask import flash


class Observer:
    _observers = []
    def __init__(self):
        self._observers.append(self)
        self._observables = {}

    def observe(self, event_name, callback):
        self._observables[event_name] = callback

class Event():
    def __init__(self, name, data, autofire = True):
        self.name = name
        self.data = data
        if autofire:
            self.fire()
    def fire(self):
        for observer in Observer._observers:
            if self.name in observer._observables:
                observer._observables[self.name](self.data)

class Food(Observer):
     def __init__(self, name, quantity, calories, expiredate):
         self.name = name
         self.quantity = int(quantity)
         self.calories = int(calories)
         self.expiredate = int(expiredate)
         Observer.__init__(self)

     def expires(self):
         if self.expiredate <= 2:
             return True
         return False

     def donate_op(self, name):
         msg = ""
         if self.expires:
            msg = "You can donate " + str(name) + " to orphans or to homeless people. Please go to donation page and choos who you want to help"
         return flash(msg)

     def compute_calories_perday(f):
         rez = f.calories / f.expiredate
         msg = "Please consume " + f.name +" "+ str(rez) +" calories per day in order to not waste food"
         return msg

     def compute_grams_perday(f):
         rez = f.quantity / f.expiredate
         msg = "Please consume " + f.name +" "+ str(rez) +" grams per day in order to not waste food"
         return msg