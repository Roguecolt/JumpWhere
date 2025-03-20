stack = []
brackets = { ')':'(',']':'[','}':'{'}
balanced = True
s=input("enter brackets sequence")
for char in s:
    if char in '({[':
        stack.append(char)
    elif char in ')}]':
        if not stack or stack[-1]!=brackets[char]:
            balanced =  False
            break
        stack.pop() 
if stack:
    balanced=False

print(balanced)