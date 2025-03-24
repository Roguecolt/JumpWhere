orgdict={'apple': 5, 'banana': 2, 'cherry': 8, 'date': 3}

items = list(orgdict.items())

for i in range(len(items)):
    for j in range(0,len(items)-i-1):
        if items[j][1]>items[j+1][1]:
            items[j], items[j + 1] = items[j + 1], items[j]

asc_dict = dict(items)

for i in range(len(items)):
    for j in range(0,len(items)-i-1):
        if items[j][1]<items[j+1][1]:
            items[j], items[j + 1] = items[j + 1], items[j]

desc_dict = dict(items)

print(asc_dict)
print(desc_dict)

