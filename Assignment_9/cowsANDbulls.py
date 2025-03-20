import random
toguess= random.randint(1000,9999)
toguessstr = str(toguess) # to iterate through the digit pos
print("Welcome to the cows and bulls game")
game_is_on = True
while game_is_on:
    guess = int(input("Guess the four digit number"))
    if guess<1000 or guess>9999: #less than 1000 is a 3 digit num and greater than 9999 is 5 so wont work
        print("Invalid input")
    if guess==toguess:
        print("Congratulations, You win !!!!")
        break
    guessstr=str(guess)
    cow=0
    bull=0
    for i in range(4):
        if toguessstr[i]==guessstr[i]:
            cow+=1
    print(f"Cow : {cow} , Bull : {4-cow}")


        
