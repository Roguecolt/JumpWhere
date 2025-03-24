samplelist = [{9:9}, {}, {}]
value = True
for i in samplelist:
    if i:
        value = False
        break

print(value)
