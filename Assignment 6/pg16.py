n=int(input("Enter size of list"))
print("Enter list elements")
numlist = [l:=int(input()) for i in range(n)]
print(numlist)
check = int(input("Enter number to search and delete"))

if check in numlist:
    numlist.remove(check)
    print(numlist)
else:
    print("Number not found")