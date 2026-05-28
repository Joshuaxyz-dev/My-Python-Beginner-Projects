# BLACK JACK PROJECT

logos = r""" ██████╗  █████╗ ███╗   ██╗████████╗███████    ╗██╗  ██╗     ██████╗ ███████╗███████╗██╗ ██████╗██╗ █████╗ ██╗         
██╔══██╗██╔══██╗████╗  ██║╚══██╔══╝██╔════╝╚██╗██╔╝       ██╔═══██╗██╔════╝██╔════╝██║██╔════╝██║██╔══██╗██║         
██║  ██║███████║██╔██╗ ██║   ██║   █████╗   ╚███╔╝        ██║   ██║█████╗  █████╗  ██║██║     ██║███████║██║         
██║  ██║██╔══██║██║╚██╗██║   ██║   ██╔══╝   ██╔██╗        ██║   ██║██╔══╝  ██╔══╝  ██║██║     ██║██╔══██║██║         
██████╔╝██║  ██║██║ ╚████║   ██║   ███████╗██╔╝ ██╗      ╚██████╔╝██║     ██║     ██║╚██████╗██║██║  ██║███████╗    
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝      ╚═════╝ ╚═╝     ╚═╝     ╚═╝ ╚═════╝╚═╝╚═╝  ╚═╝╚══════╝ 
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

import random
print(logos)
def games():
    user = []
    dealer = []
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    # initial 2 cards
    for _ in range(2):
        user.append(random.choice(cards))
        dealer.append(random.choice(cards))

    user_sum = sum(user)
    dealer_sum = sum(dealer)

    print(f"\nYour hand: {user}, total: {user_sum}")
    print(f"Dealer shows: [{dealer[0]}, ?]")  # hide dealer's 2nd card

    over = True

    # ----- PLAYER TURN -----
    while over and user_sum < 21:
        pick = input("Type 'y' to hit or 'n' to stand: ").lower()
        if pick == "y":
            new_card = random.choice(cards)
            if new_card == 11 and user_sum + 11 > 21:
                user.append(1)
            else:
                user.append(new_card)
            user_sum = sum(user)
            print(f"Your hand: {user}, total: {user_sum}")
        elif pick == "n":
            break
        else:
            print("Invalid choice. Please type 'y' or 'n'.")

        if user_sum > 21:
            over = False
            print(f"\nYOU LOSE ❌, you busted with {user} [{user_sum}]. Dealer had {dealer} [{dealer_sum}].")

    # ----- DEALER TURN -----
    while over and dealer_sum < 17:
        new_card = random.choice(cards)
        if new_card == 11 and dealer_sum + 11 > 21:
            dealer.append(1)
        else:
            dealer.append(new_card)
        dealer_sum = sum(dealer)

    # ----- FINAL RESULTS -----
    if over:
        print(f"\nFinal Hands: \nYou: {user} [{user_sum}]\nDealer: {dealer} [{dealer_sum}]")

        if user_sum > 21:
            print("YOU LOSE ❌, you busted.")
        elif dealer_sum > 21:
            print("YOU WIN 🏅, dealer busted.")
        elif user_sum == dealer_sum:
            print("DRAW 🤝")
        elif user_sum > dealer_sum:
            print("YOU WIN 🏅")
        else:
            print("YOU LOSE ❌")


# ----- GAME LOOP -----
keep_playing = True
while keep_playing:
    games()
    asks = input("\nDo you want to play again? Yes(Y) or No(N): ").lower()

    while asks != "yes" and asks != "y" and asks != "no" and asks != "n":
        print("Invalid input.")
        asks = input("Do you want to play again? Yes(Y) or No(N): ").lower()

    if asks == "yes" or asks == "y":
        keep_playing = True
    elif asks == "no" or asks == "n":
        keep_playing = False
        print("Thanks for playing!")
