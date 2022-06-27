class mobile:

    def samsung(self):
        print("Samsung is the large company in the world")

    def xiomi(self):
        print("Xiomi is the large  company in china ")

class pc(mobile):     # --> () use parentasic to create inheritance;
    def apple(self):
        print("Apple is most popular company in the world")

    def intel(self):
        print("Intel was a big processor company ,they build processor for pc")


p = pc()
p.apple()
p.intel()
p.xiomi()
p.samsung()
"""
class mobile:

    def samsung(self):
        print("Samsung is the large company in the world")

    def xiomi(self):
        print("Xiomi is the large  company in china\n ")

class pc:
    def apple(self):
        print("Apple is most popular company in the world")

    def intel(self):
        print("Intel was a big processor company ,they build processor for pc")

m = mobile()
m.samsung()
m.xiomi()
p = pc()
p.apple()
p.intel()
"""
