'''
WAP to input a tuple and input a number from user and witout using
                                     index function print all the positions where number is found.
'''
import time
print("This is a code to perform linear search in tuples.")
time.sleep(2)
a = tuple(eval(input("Enter list of numbers : ")))
b = int(input("Enter the number which you want to search : "))
d = 0
for k in range(len(a)):
    if a[k] == b:
        print("Number found at index ",k)
        d += 1
if d != 0:
    pass
else:
    print("Number not found :)")
time.sleep(3)
print("\n\n")
'''
WAP to input a list and input a number from user and witout using
                                     index function print all the positions where number is found.
'''
print("This is a code to perform linear search in list.")
time.sleep(2)
c = list(eval(input("Enter list of numbers : ")))
d = int(input("Enter the number which you want to search : "))
f = 0
for val in range(len(c)):
    if c[val] == d:
        print("Number found at index ",val)
        f += 1
if f != 0:
    pass
else:
    print("Number not found :)")

