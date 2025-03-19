cost=100
quantity = int(input("Enter quantity"))
totalcost=quantity*cost
if quantity>1000:
    print(f"{totalcost-(totalcost*0.1)}")
else:
    print(f"Totalcost is {totalcost}")