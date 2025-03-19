count=0
num_list=[]
n=int(input("Enter list size"))
print("Enter list values")
for i in range(n):
    num_list.append(input(""))


for i in num_list:
    if i>30:
        count+=1

print(count)
