import math
a=float(input("enter the value"))
b=(a*2)+2
c=math.pow(a,2)/2
d=math.sqrt(a)-(2)
print("1. double the value and increase the value by2")
print("2. square")
print("3.reduce by 2")
choice=int(input("enter the choice"))

if choice == 1:
    print("vaule",b)
elif choice == 2:
    print(c)
elif choice == 3:
    print(d)
