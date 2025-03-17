s_string=input("Enter string")

def uniqueString(s):

    word=s.split(',')
    
    return ",".join(sorted(set(word)))
                     
                     
print(uniqueString(s_string))