import turtle
from turtle import Turtle as t, Screen
import random

my_screen = Screen()
my_screen.setup(width=500, height=400)

user_bet = my_screen.textinput("Make a bet", "Which color of turtle would win the race\n(RED, YELLOW, PURPLE, ORANGE, BLUE, GREEN)?)").lower()
game = True
while game:
    if user_bet in ("red", "yellow", "purple", "orange", "blue", "green"):
        players = {
            "green": t(shape="turtle"),
            "blue": t(shape="turtle"),
            "red": t(shape="turtle"),
            "yellow": t(shape="turtle"),
            "purple": t(shape="turtle"),
            "orange": t(shape="turtle"),
        }
        distance = -100
        for player in players:
            players[player].color(player)
            players[player].penup()
            players[player].goto(x=-230, y=distance)
            distance += 40
        games = True
        while games:
            for player in players:
                random_move = random.randint(0, 10)
                players[player].forward(random_move)
                if players[player].xcor() > 230:
                    game = False
                    games = False
                    if user_bet == player:
                        print(f"You win! the winner is {player}")
                    else:
                        print(f"You lose! the winner is {player}")
        my_screen.exitonclick()
    else:
        print(f"{user_bet} is not a valid!!")
        my_screen.bye()
        turtle.bye()
        my_screen.bye()







