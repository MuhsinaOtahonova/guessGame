import random
def userGuess(upper_limit):
    attemps = 0
    target = random.randint(1, upper_limit)
    guess = int(input(f"I chose a number between 1 and {upper_limit}, can you guess? "))
    while 1:
        attemps += 1
        if target == guess:
            print(f"You got it right in {attemps} tries")
            break
        elif target > guess:
            print("Wrong, the correct answer is greater than the number you guessed")
        elif target < guess:
            print("Wrong, the correct answer is less than the number you guessed")
        
        guess = int(input("Try again: "))
    return attemps