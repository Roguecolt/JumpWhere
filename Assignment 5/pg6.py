s_string = input("Enter string")

def endWith(s):
    if len(s)<3:
        return s
    else:
        if s.endswith("ing"):
            return s+"ly"
        else:
            return s+"ing"
        
print(endWith(s_string))