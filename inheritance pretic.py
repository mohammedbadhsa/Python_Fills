from abc import ABC,abstractmethod  # -> use for abstractmethods methods import
class node:
    def __init__(self,dis1,dis2):
        self.dis1 = dis1
        self.dis2 = dis2

    def area(self):
        print("I am a area methods of shape;")

class tringle(node):
    def area(self):
        area = 0.5 * self.dis1 * self.dis2
        print("The area is :",area)

class rectangle(node):
    def area(self):
        area = self.dis1 * self.dis2
        print(area)

t1 = tringle(10,30)
t1.area()
rt1 = rectangle(35.5,45)
rt1.area()