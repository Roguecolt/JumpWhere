s_string_list=eval(input("Enter lsits"))

def returnMax(s):
    return max(s,key=len)

print(returnMax(s_string_list))