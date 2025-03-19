mixed_list = [12, "hello", 3.14, 42, "world", 7.5, 100, "Python", 8.9, 55]


int_list = []
str_list = []
float_list = []

for i in mixed_list:
    if type(i)==int:
        int_list.append(i)
    elif type(i)==str:
        str_list.append(i)
    elif type(i)==float:
        float_list.append(i)

print(int_list,float_list,str_list)