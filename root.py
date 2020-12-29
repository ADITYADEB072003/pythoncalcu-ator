def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div (x,y):
    return x/y
def mod(x,y):
    return x%y
def floor(x,y):
    return x//y
print("select the following choice")
print("1.sum")
print("2.mul")
print("3.div")
print("4.mod")
print("5.sub")
print("6.floor")
choice=int(input("enter the choice"))
a=float(input("enter the first no"))
b=float(input("enter the second no"))
if choice==1:
    print(add(a,b))
elif choice==2:
    print(mul(a,b))
elif choice==3:
    print(div(a,b))
elif choice==4:
    print(mod(a,b))
elif choice==5:
    print(sub(a,b))
elif choice==6:
    print(floor(a,b))
