dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

# result = {**dic1,**dic2,**dic3}  #method 1
# result = dic1| dic2 | dic3 #method 2

# Method 3
result = {}
dic1.update(dic2)
dic1.update(dic3)
result.update(dic1)


print(result)

