## Project name:- Guess the Number
import random
target = random.randint(1, 100)
count = 0

while True:
    userChoice = input("Guess the target or Quit : ")
    if(userChoice == "Quit"):
        break

    userChoice = int(userChoice)
    count += 1

    if(userChoice == target):
        print("Success : Correct Guess!!")
        print("You guessed it in", count, "attempts")
        break

    elif(userChoice < target):
        print("Your number was small. Take a bigger guess..")
        
    else:
        print("your number was big. Take a smaller guess..")

print("-----GAME OVER-----")
    
