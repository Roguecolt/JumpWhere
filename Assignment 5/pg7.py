s_string = input("Enter string")

def swapSubstring(s):
    notindex = s.find('not')
    poor = s.find('poor')

    if notindex<poor:
        s = s[:notindex]+"good"+s[poor+4:]

    return s

print(swapSubstring(s_string))