
















"""
numberoflatter = 0
numberofdigits = 0
numberofword = 0

text = input("Enter some text :")
for i in text:
    i.lower()
    if i >= 'a' and  i <= 'z':
        numberoflatter = numberoflatter + 1

    elif i >= '0' and i <= '9':
        numberofdigits = numberofdigits + 1

    elif i == " ":
        numberofword = numberofword + 1

print("number of latter :",numberoflatter,"\nnumber of digits :"
      ,numberofdigits,"\nnumber of word :",numberofword)

"""




"""
---> string number convert to list ..!

n = input("Enter some string :")
list = n.split()
print(list)
"""

"""
 ---> 1st input some string number and then , convert to list and all number do sum .!

n = input("Enter  some string to convert lsit :")
list = n.split()
sum = 0
for num in list:
    sum = sum + int(num)
print(sum)

"""