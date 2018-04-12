import random

def randomNumGenerator(lowerLimit, upperLimit, howMany=1, multiplier=1):
    for x in range(howMany):
        print (random.randint(lowerLimit, upperLimit)* multiplier)
    
    

if __name__ == "__main__":
    print("Welcome to a random number generator")
    limits = input("What is the lower and upper limits of random number? ")
    limits = limits.split()
    lowerLimit = int(limits[0])
    upperLimit = int(limits[1])
    print("{} {}".format(lowerLimit, upperLimit))

    howMany = int(input("How many random numbers you wish to generate? "))

    multiplier = input("Is there any common factor? If yes, what is that?")
    if multiplier == "":
        randomNumGenerator(lowerLimit, upperLimit, howMany)
    else:
        multiplier = int(multiplier)
        randomNumGenerator(lowerLimit, upperLimit, howMany, multiplier)
