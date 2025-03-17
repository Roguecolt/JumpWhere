s_string=input("Enter string")

def upperstring(s):
    count=0
    if len(s)<4:
        return -1
    
    for i in range(4):
        if s[i].isupper():
            count+=1
            if count>1:
                return s.upper()

print(upperstring(s_string))