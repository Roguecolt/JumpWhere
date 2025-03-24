sample = [[1, 2, 3], [2, 4, 5], [1, 1, 1]] 

lambdasort = sorted(sample,key=lambda x : sum(x))
print(lambdasort)