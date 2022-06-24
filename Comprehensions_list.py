
list1 = [12,32,42,12,42,12,43]

# [expression for item in list]

#result = [x*x for x in list1]
#print(result)

result = [x for x in list1 if x%2==0]
print(result)
