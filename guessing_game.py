import random
secret_number = random.randint(1, 100)
guesses = 0
print("I'm thinking of a number between 1 and 100!")
while guesses < 15:
    guess = int(input("Take a guess: "))
    if guess < 1 or guess > 100:
        print("Please guess a number between 1 and 100.")
        continue
    guesses += 1
    if guess < secret_number:
        print(f"Your guess is too low. {15 - guesses} {'guess' if (15 - guesses) == 1 else 'guesses'} remaining.")
    elif guess > secret_number:
        print(f"Your guess is too high. {15 - guesses} {'guess' if (15 - guesses) == 1 else 'guesses'} remaining.")
    else:
        break  # This means the guess is correct   
if guess == secret_number:
    print(f"Congratulations! You guessed the number in {guesses} guesses.")
else:
    print(f"Sorry, you've used all your guesses. The number was {secret_number}.")