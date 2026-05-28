
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
print("welcome to Dantex Official Rock Paper Scissors Game")
you = input("R for ROCK\nP for PAPER\nS for SCISSORS\n: ").lower()

game = [rock, paper, scissors]
games = ['ROCK', 'PAPER', 'SCISSORS']
cmp_choice = random.randint(0, 2)

if you == "r" and cmp_choice == 0:
    print(f"Computer chose {games[cmp_choice]}\n {game[cmp_choice]}")
    print(f"you chose {games[0]}\n{game[0]} ITS A DRAW")
elif you == "r" and cmp_choice == 1:
    print(f"Computer chose {games[cmp_choice]}\n {game[cmp_choice]}")
    print(f"you chose {games[0]}\n{game[0]} YOU LOSE")
elif you == "r" and cmp_choice == 2:
    print(f"Computer chose {games[cmp_choice]}\n {game[cmp_choice]}")
    print(f"you chose {games[0]}\n{game[0]} YOU WIN")
elif you == "p" and cmp_choice == 0:
    print(f"Computer chose {games[cmp_choice]}\n {game[cmp_choice]}")
    print(f"you chose {games[1]}\n{game[1]} YOU WIN")
elif you == "p" and cmp_choice == 1:
    print(f"Computer chose {games[cmp_choice]}\n {game[cmp_choice]}")
    print(f"you chose {games[1]}\n{game[1]} ITS A DRAW")
elif you == "p" and cmp_choice == 2:
    print(f"Computer chose {games[cmp_choice]}\n {game[cmp_choice]}")
    print(f"you chose {games[1]}\n{game[1]} YOU LOSE")
elif you == "s" and cmp_choice == 0:
    print(f"Computer chose {games[cmp_choice]}\n {game[cmp_choice]}")
    print(f"you chose {games[2]}\n{game[2]} YOU LOSE")
elif you == "s" and cmp_choice == 1:
    print(f"Computer chose {games[cmp_choice]}\n {game[cmp_choice]}")
    print(f"you chose {games[2]}\n{game[2]} YOU WIN")
elif you == "s" and cmp_choice == 2:
    print(f"Computer chose {games[cmp_choice]}\n {game[cmp_choice]}")
    print(f"you chose {games[2]}\n{game[2]} ITS A DRAW")
else:
    print(f"your input {you} is INVALID, please its R for ROCK, P for PAPER, d"
          f"S for SCISSORS")


