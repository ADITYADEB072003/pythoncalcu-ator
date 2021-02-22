mn={}

for i in range(3):
    r=eval(input("enter the roll no"))
    m=eval(input("enter the marks"))
    mn[r]=m
print("created dictionery")
print(mn)
print("to modify marks")
r2=int(input("enter the no"))
if r2 in mn:
    mn[r]=int(input("enter the marks"))
else:
      print("not present")
    
print(mn)
print("to modify marks")
r3=int(input("enter the no"))
if r3 in mn:
    mn[m]=int(input("enter the roll"))
else:
      print("not present")
print(mn)
