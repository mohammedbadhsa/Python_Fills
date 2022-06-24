from random import randint

for x in range(1,11):
    guessnumber = int(input("Enter The Guss Number in 1 ot 10 :"))
    randomnumber = randint(1,10)
    if guessnumber == randomnumber:
        print("YOU WIN !")

    else:
        print("YOU LOSE !")
        print("YOUR Random_Number :",randomnumber)






"""
--->python pattarn
n = 17
for i in range(n):
    i = ((i*2-1)*"*")
    print(i)
"""
"""
-->python pattan
n = 7
for i in range(n):
    i = i*"*"
    print(i)
"""