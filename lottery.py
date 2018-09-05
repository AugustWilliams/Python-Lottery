def pickNumbers():
    print("Pick five numbers between 1 and 50, seperated by commas")
    numbersPicked = input("...")
    numbersPicked = numbersPicked.replace(" ", "")
    numbersPicked = numbersPicked.split(",")
    return numbersPicked

def rollNumbers():
    from random import randint
    rolledNumbers, count = [], 5
    while count > 0:
        choice = randint(1,50)
        if choice not in rolledNumbers:
            rolledNumbers.append(choice)
            count -= 1
    print (rolledNumbers)
    return rolledNumbers

def checkNumbers(numbersPicked, rolledNumbers):
    prizes = {0:"£0", 1:"£2.50", 2:"£5", 3:"£10", 4:"£50", 5:"£100"}
    matchedCount = 0
    for element in numbersPicked:
        if element in rolledNumbers:
            matchedCount += 1
    print ("")
    print ("Your numbers:", numbersPicked)
    print ("Rolled Numbers:", rolledNumbers)
    print ("You matched", matchedCount, "numbers.")
    print ("You won", prizes[matchedCount])

numbersPicked = pickNumbers()
rolledNumbers = rollNumbers()
checkNumbers(numbersPicked, rolledNumbers)
