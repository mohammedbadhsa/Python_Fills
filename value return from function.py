def large(a,b):
    if a > b :
        return("the large value is a")
    else:
        return("the large value is b")

#result = large(200,31)
#print(result)
#print(large(13,11))
#large(100,321) --> jokon condition ar kase print deya thakbe thokon kaj korbe function call !!

# ---> xargs in function
'''
def fun(*number):   # --->  *_name use for xargs  argument !!
    sum = 0
    for x in number:# ---> use for loop in funciton !!
      sum = sum + x
    print(sum)

fun(10,20,59)
'''
'''
# ---> xxargs use in  function !!

def student(**datails):
    print(datails["name"])

student(id = 100, name = "durjoy bhai")
'''