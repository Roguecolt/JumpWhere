import random

with open("hangman.txt","r") as wordsfile:
    words = wordsfile.read().split()

def random_word(words):
    word = random.choice(words)
    return word

def user_guess(letter , wordletter):
    if letter not in wordletter:
        return False
    return True
    


game_is_on=True
while game_is_on:
    print("Welcome to Hangman!!!")
    word = random_word(words)
    # print(word)
    wordletter = list(word)
    # print(wordletter)
    guesses=6
    guessed_letter = set()
    while guesses>0:
        print("Guess your letter")
        guess = input().lower()

        if guess in guessed_letter:
            print("You have already guessed that letter")
            continue

        guessed_letter.add(guess)
        display_word = [letter if letter in guessed_letter else "_" for letter in word]
        print(" ".join(display_word))
        if  not user_guess(guess, wordletter):
            print("Incorrect")
            guesses-=1
            print(f"You have remanining {guesses} guesses")
            if guesses ==0:
                print("Game over\n")
                choice = input("Do you wish to restart y/n")
                if choice.lower()=='y':
                    game_is_on=True
                else:
                    game_is_on=False
                    break
        
        if "".join(display_word) == word:
            print("Congrats!! You win")
            choice = input("Do you wish to restart y/n")
            if choice.lower()=='y':
                break
            else:
                game_is_on=False
                break
        



