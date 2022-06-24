
# ---> map and filter function in python !!
"""
def myf(x):
    print(x*x)

num = [1,4,5,8,9]
result = list(map(myf,num))  # --> map(akta function ar akta list) rakte pare map akta interactive object
                                    ja (__,__) 2t paramitter nia kaj kore thake!
print(result)
"""

def myf1(x):
    return x*x*x
mylist = [10,20,30,40]

result = list(map(myf1,mylist))
print(result)
