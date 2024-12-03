import  random

# Print Logo

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
attempts = 0
game_continue = True

def game(n):
    # global  attemps
    print(f"You have {n} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    return guess

# generate a random number 1-100
number = random.randint(1,100)

if level == 'easy':
    attempts = 10
    while attempts > 1 and  game_continue :
        guess_number = game(attempts)
        attempts -=1
        print(number)
        if attempts < 1 :
            print("You've run out of guesses.")
            game_continue = False

        if guess_number > number:
            print("Too High!")
            game(attempts)
        elif guess_number < number :
            print("Too Low")
            game(attempts)
        else:
            print(f"You got it! The answer was {number}.")
            game_continue = False

elif level == 'hard' :
    print("")
else:
    print('Invalid Level! \nTry Again!!')


