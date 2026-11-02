import random 

print(" \nWelcome to the Number Guessing Game!\n ")
print("\nI'm thinking of a number between 1 and 100.\n ")

secret_number = random.randint(1,100)


attempts = 0

while True:
    print(" \nEnter your guess: ")
    guess = input()

    try:
        guess_int = int(guess)
    except ValueError:
        print("Please enter a valid number!")
        continue

    if guess_int < 1 or guess_int > 100:
        print("please enter a number between 1 and 100")
        continue


    print("Your guess is: "+ guess)
    attempts = attempts + 1
    
    if guess_int > secret_number:        
        print(" Too High!")    
    elif guess_int < secret_number: 
        print("Too Low!")
    else: 
        print(" Correct! You Won! ")
        print(f"You guessed the answer in {attempts} attempts!")
        break 

    
