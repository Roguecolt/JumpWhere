even=[]
odd=[]
prime = []
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

for i in range(1,101):
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)

    if is_prime(i):
        prime.append(i)

print(prime,even,odd,sep="\n")
