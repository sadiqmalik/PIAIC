import random

# Guess the random number
def guessRandomNumber():
    # number of elements as input
    random_number = random.randint(1, 50)

    for i in range(1, 4):
        while True:
            try:
                number = int(input("\nGuess the number 1-50: "))
                break
            except ValueError:
                print("Only number allowed!")
        
        if (number == random_number):
            print("Great! You guessed it correctly.")
            break

        print("Bad luck!")
    
    print("\nRandom number was: ", random_number)

print("\n********************* Guess Random Number *********************")
guessRandomNumber()
