# while loops in python program

i = 1
while i <= 100:
    #print("Mohammad Badsha 07","Durjoy bhai","adib mohammed hamim")
    i = i + 1

# using while loops to 1 to 100 number sum / jok korar jonno use hobe ..
sum = 0
i = 1
while i <= 20:
    sum = sum + i
    i = i + 1
print(sum)

n = int(input("Enter the value of  n :"))
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
#print(sum)

#--> user input some string a convert to int finally sum all numbers

number = input("Enter some number :") # 4565
#total = int(number[0])
total = 0
i = 0
while i < len(number):
    total += int(number[i])
    i += 1
print(total)

some_text = input("Enter the some text : ")
total = 0
i = 0
while i < len(some_text):
    total = total + int(some_text[i])
    i = i + 1

print(total)

