s_string = input("Enter string")

length = len(s_string)

if length<2:
    print("")
else:
    print(s_string[0:2]+s_string[-2:])