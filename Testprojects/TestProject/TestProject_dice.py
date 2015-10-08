import random
while True:
    maxsides = int(input("how many sides does the die have?: "))
    numofthrows = int(input("how many times do you roll the dice?: "))

    for i in range(numofthrows):
        print random.randint(1, maxsides)
