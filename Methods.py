

class methods:
    Name = ""
    Roll = ""

    def set_value(self,Name,Roll):
        self.Name = Name
        self.Roll = Roll

    def myfunc(self):
        print(f"Name : {self.Name} , Roll :{self.Roll}")

badsha = methods()
badsha.set_value("Mohammed Badsha",483017)
badsha.myfunc()

jibon = methods()
jibon.set_value("Mohammed jibon",483021)
jibon.myfunc()


