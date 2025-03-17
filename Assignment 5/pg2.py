s_string=input("Enter string")

h_map = {}
for s in s_string:
    if s not in h_map:
        h_map[s]=1
    else:
        h_map[s]+=1

print(h_map)