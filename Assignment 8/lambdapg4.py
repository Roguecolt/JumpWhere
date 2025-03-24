string=input("Enter string")

ifstart = lambda x : True if string[0]==x else False

checker = input("Enter letter to check")
print(ifstart(checker))