import random
while True:
    
    
    minnum = int(input("What is the minimum number that the AI chooses? : "))
    maxnum = int(input("What is the maximum number that the AI chooses? : "))
    actualnum = random.randint(minnum, maxnum)
    numguess = False

    while numguess == False:
        numberguess = int(input("What number do you think the AI chose? : "))
        print (actualnum)

        if numberguess == actualnum:
            print ("You guessed the number!")
            numguess = True
        elif numberguess > actualnum:
            print ("The number you entered is", (numberguess - actualnum), "higher than the actual number")
        elif numberguess < actualnum:
            print ("The number you entered is", (numberguess + actualnum), "lower than the actual number")
