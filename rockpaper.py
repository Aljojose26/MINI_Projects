import random

userwins = 0
computerwins = 0

options = ["Rock", "paper", "scissors"]

while True:
    user_input = input("Type rock pape scissors or q ").lower()
    if user_input == "q":
        break
    if user_input not in options :
        continue
    random_number = random.randint(0,2)
    #rocl 0 paper 1 scissors 2
    computer_pick = options[random_number]
    print("computer picked", computer_pick + ".")

    if userwins == "rock" and computer_pick == "scissors":
        print("you won")
        userwins +=1

    elif userwins == "paper" and computer_pick == "rock":
        print("you won")
        userwins +=1

    elif userwins == "scissors" and computer_pick == "paper":
        print("you won")
        userwins +=1
    else:
        print("COMPUTER won")
        computerwins +=1


print(f"you won",userwins,"times" )
print("the computer wins", computerwins)
print("Goodbye")