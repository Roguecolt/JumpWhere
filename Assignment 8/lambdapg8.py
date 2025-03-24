validstring = lambda x : True if (len(x)>=10 and 
                                  any(c.islower() for c in x) and
                                  any(c.isupper() for c in x) and
                                  any(c.isdigit() for c in x)
) else False

string = input("Enter string")
print(validstring(string))