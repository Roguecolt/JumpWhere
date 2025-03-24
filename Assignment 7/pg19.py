samplelist= [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
newlist = []
for i in samplelist:
    if i not in newlist:
        newlist.append(i)

print(newlist)