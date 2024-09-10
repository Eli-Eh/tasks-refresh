class Students:
    def __init__(self, potions, history, herbology, transfiguration):
        self.potions = potions
        self.history = history
        self.herbology = herbology
        self.transfiguration = transfiguration

    def avg(self):
        return (self.herbology + self.potions + self.history +self.transfiguration)/4

stud1 = Students(56,89,6,15)
stud2 = Students(89,67,81,90)
stud3 = Students(51,40,60,72)

print(stud1.avg())
print(stud2.avg())
print(stud3.avg())
