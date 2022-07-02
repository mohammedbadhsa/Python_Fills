# build in polymorphism in python
"""
print(len("Anisul islam"))
print(len("Mohammed BADSHA"))
print(len([10,94,920,593,5334]))
"""

def add(a, b, c):
    result = a*b*c
    print(result)
#add(10,20,30)
#add(20,50000,6414)

class polymorphism:
    name = ""
    roll = ""
    cgpa = ""

    def __init__(self,name,roll,cpga):
        self.name = name
        self.roll = roll
        self.cgpa = cpga
    def display(self):
        print(f" Name : {self.name}\n Roll : {self.roll}\n CGPA : {self.cgpa}")

ob1 = polymorphism("Mohammed badsha",483017,3.64)
ob1.display()


