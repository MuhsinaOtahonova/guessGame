import random

def pcGuess(upper_limit):
    attemps = 0
    lower_limit = 1
    while 1:
        attemps += 1
        if lower_limit != upper_limit:
            guess = random.randint(lower_limit, upper_limit)
        else:
            guess = upper_limit
        result = input(f"{guess}, if the number you entered is greater than I predicted, enter '+' If it is smaller, enter '-' If it is the same, enter 'true'.")
        if result == "+":
            lower_limit = guess + 1
        elif result == "-":
            upper_limit = guess - 1
        else:
            print(f"I got it right in {attemps} tries")
            break
    return attemps