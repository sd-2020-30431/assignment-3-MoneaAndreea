class Donations:
    def __init__ (self, foodname, quantity, option, user):
        self.foodname = foodname
        self.quantity = int(quantity)
        self.option = option
        self.user = user
