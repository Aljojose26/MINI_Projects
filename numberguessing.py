import random

top_of_range = input("type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("please type a number larger than 0 nect  time")
        quit()
else:
    print("please type a number")
    quit()

random_number = random.randint(0,20)
guesses = 0

while True:
    guesses += 1
    user_guess = input("make a guess")
    if user_guess.isdigit():
        user_guess = int(user_guess)


    else:
        print("please type a number nect time")
        continue

    if user_guess == random_number:
        print("you got it correct")
        break
    else:
        print("you got it wrong")

print(f"you got it in {guesses}")



