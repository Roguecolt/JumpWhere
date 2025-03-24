sample =  [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}] 

lambsort = sorted(sample , key= lambda x :int(x['model']), reverse = True)

print(lambsort)