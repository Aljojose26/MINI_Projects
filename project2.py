print("Welcom to my computer Quiz!")

playing = input("Do you want to play yes or no  ")
if playing.lower() != "yes":
    quit()

print("okay lets play ")
score = 0

answer = input(" What does cpu stand for ? ")
if answer.lower() == "central processing unit":
    print("Correct")
    score += 1

else :
    print("not correct")
answer = input("What does gpu stand  ")
if answer.lower() == "graphic processing unit":
    print("correct")
    score += 1

else :
    print("not correct")

answer = input("what does ram stand for   ")
if answer.lower() == "random access memory ":
    print("Correct")
    score += 1

else :
    print("not correct")

answer = input(" What does PSU stand for ")
if answer.lower() == "power supply unit":
    print("Correct")
    score += 1

else :
    print("not correct")
print(f"you got the total{score/4*100} score  correct" )







