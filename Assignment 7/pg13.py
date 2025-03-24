sampledict = {
    "a": 10,
    "b": 25,
    "c": 5,
    "d": 42,
    "e": 18
}

noDupdict = {}

for key , value in sampledict.items():
    if value not in noDupdict.values():
        noDupdict[key] = value

print(f"")