sample =  [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

lamsort = sorted(sample, key= lambda x: x[1], reverse=False)
print(lamsort)