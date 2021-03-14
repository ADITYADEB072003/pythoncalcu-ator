#asset
cash=int(input("enter the cash"))
account=int(input("enter the account"))
inventory=int(input("enter the invtory"))
#liabilities
accountpayable=int(input("enter the amt payable"))
loan=int(input("enter the loan amt"))
accuredliabilties=int(input("liabilites"))
totalasset=cash+account+inventory
totalliabilites=accountpayable+loan+accuredliabilties
#asset=liabilites+capital
if totalasset>totalliabilites:
    capital1=totalasset-totalliabilites
    print("working capital1=",capital1)
else:
    if totalliabilites>totalasset:
        capital2=totalliabilites-totalasset
        print("working capital2",capital2)
