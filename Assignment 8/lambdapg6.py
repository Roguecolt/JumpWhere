divisible = lambda x : x if x%13==0 or x%19==0 else None

sample = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
divisiblelist = [x for x in sample if divisible(x) is not None]




print(divisiblelist)