print("Welcome to the PC Components Quiz!")
print("I will think of a PC component, and you have to guess what it is.")

playing = input("Would you like to play? (yes/no)")
playing = playing.lower().strip()

print("Great! Let's start!")

if playing != "yes":
    print("Okay, maybe next time!")
    quit()

score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    score += 1
    print("Correct!")
else:
    print("Incorrect. The correct answer is 'Central Processing Unit'.")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    score += 1
    print("Correct!")
else:
    print("Incorrect. The correct answer is 'Graphics Process Unit'.")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    score += 1
    print("Correct!")
else:
    print("Incorrect. The correct answer is 'Random Access Memory'.")

answer = input("What does SSD stand for? ")
if answer.lower() == "solid state drive":
    score += 1
    print("Correct!")
else:
    print("Incorrect. The correct answer is 'Solid State Drive'.")

answer = input("What does HDD stand for? ")
if answer.lower() == "hard disk drive":
    score += 1
    print("Correct!")
else:
    print("Incorrect. The correct answer is 'Hard Disk Drive'.")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply unit":
    score += 1
    print("Correct!")
else:
    print("Incorrect. The correct answer is 'Power Supply Unit'.")

print(f"You got {score} out of 6 questions correct. {score / 6 * 100}%")
print("Thanks for playing the PC Components Quiz!")
