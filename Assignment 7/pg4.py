orgdict={'apple': 5, 'banana': 2, 'cherry': 8, 'date': 3}
n=input("enter key")
def if_key(orgdict,n):
    if n in orgdict.keys():
        print("Key exists")
    else:
        print("Key does not exist")

if_key(orgdict,n)