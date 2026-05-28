import random

attempts = 10


def easy():
    return attempts


def hard():
    return attempts - 5


def game():
    print("Welcome to Dantex Official Guess Game")
    print("I'm thinking of a number from 1 - 100")
    difficulty = input("Choose a difficulty: Type EASY or HARD: ").lower()
    lives = 0
    if difficulty == "easy":
        lives = easy()
    elif difficulty == "hard":
        lives = hard()
    over = True
    chose = random.randint(1, 100)
    while over:
        if lives != 0:
            print(f"You have {lives} attempts remaining")
            guess = int(input("Make a guess: "))
            if lives != 0 and chose > guess:
                lives -= 1
                if lives == 0:
                    print("Too low")
                else:
                    print(f"Too low\nGuess again.")
            elif lives != 0 and chose < guess:
                lives -= 1
                if lives == 0:
                    print("Too high")
                else:
                    print(f"Too high\nGuess again.")
            elif lives != 0 and chose == guess:
                print(f"You got it! The answer is {guess}")
                over = False
        else:
            print(f"You've run out of guesses! You lose\n ANSWER: {chose}")
            over = False


game()