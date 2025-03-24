x = {'key1': 1, 'key2': 3, 'key3': 2}
y =  {'key1': 1, 'key2': 2}



for key, value in x.items():
    if (key,value) in y.items() :
        print(f"{key} : {value} is present in both x and y")
