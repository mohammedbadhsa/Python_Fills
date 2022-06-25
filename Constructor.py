

class class2:
    Name = ""
    Roll = ""
    GPA = ""

    def __init__(self,Name,Roll,CGPA):
        self.Name = Name
        self.Roll = Roll
        self.GPA = CGPA

    def printout(self):
        print(f"Name : {self.Name}\nRoll : {self.Roll}\nCGPA : {self.GPA}")


hamim = class2("Mohammad Hamim",16321,4.00)
hamim.printout()


class class1:
    Name = ""
    Roll = ""
    GPA = ""

    def __init__(self,Name,Roll,GPA): # __init__ -> using constuctor methods ;.
        self.Name = Name
        self.Roll = Roll
        self.GPA = GPA

    def runvalue(self):
        print(f"Student Name : {self.Name} \nStudent Roll : {self.Roll} \nStudent GPA : {self.GPA}")

durjoy = class1("Durjoy Bhomik",302,3.88)
durjoy.runvalue()

