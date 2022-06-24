"""
try:                         # try: use for jekane error hoite pare oikane try ar under raika next program
                                # ran hoite deya jabe
    list = [1, 0, 33, 42, 43]

    result = list[0] / list[5]

except ZeroDivisionError:                   # except jei error tar nam dite hobe tar under kiso statement dite parmo ;
    print("we found some error man")

finally:                                       # finally under thaka sob code ran hobe try: o except jai hok na kno !
    print(' Name : Mohammed Badsha\n Roll : 483017')
"""
try:
    a = int(input("Enter the value of a:"))
    b = int(input("Enter the value fo b :"))

    result = a / b
    print(result)

except (ZeroDivisionError, IndexError) :
    print("your enter the rong code")

finally:
    print("successfully")
