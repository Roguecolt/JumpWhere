s_string= input("Enter string")

def swapCommadot(s):
    s = s.replace('.', '#') 
    s = s.replace(',', '.') 
    s = s.replace('#', ',') 
    return s



print(swapCommadot(s_string))
