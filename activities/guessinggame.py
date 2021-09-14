import random

comp_number = random.randrange(1, 11)

while True:
    while True:
        try:
            guessed_number = int(input("Guess a number between 1 and 10: "))
            break
        except ValueError:
            print("You didn't enter a number")
        except:
            print("An unknown error occurred")

    if guessed_number > 10 or guessed_number < 1:
        print("***selected number outside of range***")
    elif guessed_number == comp_number:
        print("You Got It!!!")
        break
