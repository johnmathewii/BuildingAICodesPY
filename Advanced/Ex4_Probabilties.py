import random

def main():

    prob = 0.2
    c = random.random()

    if c < prob:
        if c < 0.1:
            favourite = "cats"
        else:
            favourite = "bats"     
    else:
        favourite = "dogs"
      
    print("I love " + favourite) 


main()
