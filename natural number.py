n=int(input("enter the term"))
sumeven =0
sumodd=0
sum=0
print("evenno")
for i in range(1,n+1):
    sum=sum+i
    if i%2==0:
        sumeven+=i
        print(i)
else:
    print("odd no")
    for i in range(1, n + 1):
        if i % 2 != 0:
            sumodd += i
            print(i)


print("sum of even no",sumeven)
print("sum of odd no",sumodd)
print("sum",sum)
