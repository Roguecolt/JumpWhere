s_string= input("Enter string")
def removeDuplicates(s):
    result = s[0]  
    for i in range(1, len(s)):
        if s[i] != s[i - 1]:  
            result += s[i]
    return result


print(removeDuplicates(s_string))