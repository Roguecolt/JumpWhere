s_string = input("Enter string")
s= input("Enter traget character")
n_string=""
count=0
for i in range(len(s_string)):
    if s== s_string[i]:
        count+=1
        if count>1:
            n_string+='$'
    n_string+=s_string[i]

print(n_string)