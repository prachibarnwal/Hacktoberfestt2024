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
