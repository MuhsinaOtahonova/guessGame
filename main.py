import userGuess as ug
import pcGuess as pg


result =  "yes"
user = 0
pc = 0
while result.lower() == "yes":
    upper_limit = int(input("I will guess a number between 1 and the number you enter. Please enter a number"))
    user = ug.userGuess(upper_limit)
    input(f"Think of a number between 1 and {upper_limit}, and I'll try to guess it. Press any key when you're ready.")
    pc = pg.pcGuess(upper_limit)
    result = input("Would you like play again? Yes, No")
if user > pc:
    print("I won")
elif user < pc:
    print("You won")
else:
    print("We both won")