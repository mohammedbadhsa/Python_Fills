
#---->using methods in class to easy program

class Studentlist:
    Student_Name = ""
    Student_Roll = ""
    Student_Dept = ""

    def set_value(self,Name,Roll,Dept):
        self.Student_Name = Name
        self.Student_Roll = Roll
        self.Student_Dept = Dept

    def information(self):
        print(f" Student Name : {self.Student_Name} \n Student Roll : {self.Student_Roll} \n "
              f"Student Departmetn :{self.Student_Dept}")


durjoy = Studentlist()
durjoy.set_value("Durjoy",1024,"ME IN DUET")
durjoy.information()



"""
class methods:
    Name = ""
    Roll = ""

    def set_value(self,Name,Roll):
        self.Name = Name
        self.Roll = Roll

    def myfunc(self):
        print(f"Name : {self.Name} , Roll :{self.Roll}")

badsha = methods()
badsha.set_value("Mohammed_Badsha",483017)
badsha.myfunc()


jibon = methods()
jibon.set_value("Mohammed_Jibon",483021)
jibon.myfunc()
"""

