yr=int(input("enrteer"))
if yr%100==0:
    if yr%400==0:
        leap=True
    else:
        leap=False
elif yr%4==0:
    leap=True
else:
    leap=False
if leap==True:
    print(yr,"leap year")
else:
    print(yr,"not a leap year")
    
