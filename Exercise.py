
class tringle:
    base = ""
    height = ""

    def __init__(self,base,height):   # --> __init__ holo akta constructor methods ja function a use kora jay ar ki .!
        self.base = base
        self.height = height

    def tringle_area(self):
        area = 0.5*self.base*self.height
        print("Area is :",area)


t1 = tringle(10,20)     # akane t1 holo akta object ja bitor tringle class ase and constructor
                        # use koira aikane vaue pass korci .
t1.tringle_area()
t2 = tringle(20,30)
t2.tringle_area()


