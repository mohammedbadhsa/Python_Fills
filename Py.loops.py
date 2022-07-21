
list = [11,22,42,54,45,54,64]
#print(list)

    index = 0
    while index <=4 :
    print(list[index])
    index = index + 1


sum = 0 
for x in list:
    sum = sum + x
#print(sum)

# 1+2+3+4+5.....+n
n = int(input("enter the value of n:"))
sum = 0
for i in range(1,n+1,1):
    sum = sum + i
#print(sum)


# ---> 2+4+6+.....+n
n = int(input("Enter The value fo n:"))
sum = 0
for x in range(2,n+1,2):
    sum = sum + x
#print(sum)

#1*1+2*2+3*3+......+n*n
n = int(input("Enter the value fo n:"))
sum = 0
for x in range(1,n+1,1):
    sum = sum + x*x
#print(sum)

#1*2*3*....*n
n = int(input("Enter the value fo n:"))
sum = 1
for x in range(1,n+1,1):
    sum = sum * x
#print(sum)


