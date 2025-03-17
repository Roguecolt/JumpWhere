s_string=input("Enter string")

def multiple(s_string):
    if len(s_string)%4==0:
        return s_string[::-1]
    
print(multiple(s_string))