'''
roll = [483017,483021,483010,482949]
name = ["Mohammad Badsha","Mohammad jiob"," Mohammad Abdullah","MD : Moniruzzaman"]

students = list(zip(roll,name,))  # --> zip function use kore amra 2ti list k akta
                                    # tupule a convert korte pari jekane akta akta kore item jabe zip functin a .
print(students)

print(list(zip(roll,name,)) )
'''

n = int(input("Enter the value of n :"))
fact = 1
for x in range(1,n+1):
    fact = fact * n

print("The factorials is :",fact)

