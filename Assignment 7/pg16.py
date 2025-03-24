sampledict = {'a': 50, 'b': 20, 'c': 80, 'd': 40, 'e': 100}

top3 = sorted(sampledict.items(), key= lambda x : x[1], reverse=True)[:3]

print(top3)