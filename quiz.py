print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()
print("Okay! Let's play :)")
score = 0

answer = input("What does MVC stands for?")
if answer == "model view control":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does OOP stand for?")
if answer == "object oriented programming":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does TDD stand for?")
if answer == "test driven development":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does BDD stand for?")
if answer == "behaviour driven development":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
print("You got " + str(score) + "questions correct!")
print("You got " + str((score / 4) * 100) + "%.")