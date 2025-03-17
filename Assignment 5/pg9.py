s_string=input("Enter string")
l=int(input("Enter index"))
n_string=''
def deleteChar(s_string,n_string,l):
    for i in range(len(s_string)):
        if i==l:
            continue
        n_string+=s_string[i]
    return n_string

print(deleteChar(s_string,n_string,l))