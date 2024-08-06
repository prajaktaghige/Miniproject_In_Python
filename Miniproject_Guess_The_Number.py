import random


target=random.randint(1,100)

while True:
    userChoice=input("guess the target or Quit: ")
    if(userChoice=="Quit"):
        break
    if(userChoice == target):
        print("sucess: correct Guess!!")
        break
    if(userChoice<target):
        print("Your number was to small.take bigger guess..")
    else:
        print("Your number was to big.take smaller guess..")
        
print("___Game Over__")
