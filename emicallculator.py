import math
p=float(input("enter the pricnicpal amt"))
r=float(input('enter the rate of interest'))
n=float(input("enter the no of installment"))
mr=r/(12*100)
emi=p*mr*(1+mr)**n/(((1+mr)**n)-1)
print("emi",emi)