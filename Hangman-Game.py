stages = [
    r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''',
    r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''',
    r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''',
    r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''',
    r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''',
    r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''',
    r'''
  +---+
  |   |
      |
      |
      |
      |
=========
'''
]

word_list = [
    'abruptly',
    'absurd',
    'abyss',
    'affix',
    'askew',
    'avenue',
    'awkward',
    'axiom',
    'azure',
    'bagpipes',
    'bandwagon',
    'banjo',
    'bayou',
    'beekeeper',
    'bikini',
    'blitz',
    'blizzard',
    'boggle',
    'bookworm',
    'boxcar',
    'boxful',
    'buckaroo',
    'buffalo',
    'buffoon',
    'buxom',
    'buzzard',
    'buzzing',
    'buzzwords',
    'caliph',
    'cobweb',
    'cockiness',
    'croquet',
    'crypt',
    'curacao',
    'cycle',
    'daiquiri',
    'dirndl',
    'disavow',
    'dizzying',
    'duplex',
    'dwarves',
    'embezzle',
    'equip',
    'espionage',
    'euouae',
    'exodus',
    'faking',
    'fishhook',
    'fixable',
    'fjord',
    'flapjack',
    'flopping',
    'fluffiness',
    'flyby',
    'foxglove',
    'frazzled',
    'frizzled',
    'fuchsia',
    'funny',
    'gabby',
    'galaxy',
    'galvanize',
    'gazebo',
    'giaour',
    'gizmo',
    'glowworm',
    'glyph',
    'gnarly',
    'gnostic',
    'gossip',
    'grogginess',
    'haiku',
    'haphazard',
    'hyphen',
    'iatrogenic',
    'icebox',
    'injury',
    'ivory',
    'ivy',
    'jackpot',
    'jaundice',
    'jawbreaker',
    'jaywalk',
    'jazziest',
    'jazzy',
    'jelly',
    'jigsaw',
    'jinx',
    'jiujitsu',
    'jockey',
    'jogging',
    'joking',
    'jovial',
    'joyful',
    'juicy',
    'jukebox',
    'jumbo',
    'kayak',
    'kazoo',
    'keyhole',
    'khaki',
    'kilobyte',
    'kiosk',
    'kitsch',
    'kiwifruit',
    'klutz',
    'knapsack',
    'larynx',
    'lengths',
    'lucky',
    'luxury',
    'lymph',
    'marquis',
    'matrix',
    'megahertz',
    'microwave',
    'mnemonic',
    'mystify',
    'naphtha',
    'nightclub',
    'nowadays',
    'numbskull',
    'nymph',
    'onyx',
    'ovary',
    'oxidize',
    'oxygen',
    'pajama',
    'peekaboo',
    'phlegm',
    'pixel',
    'pizazz',
    'pneumonia',
    'polka',
    'pshaw',
    'psyche',
    'puppy',
    'puzzling',
    'quartz',
    'queue',
    'quips',
    'quixotic',
    'quiz',
    'quizzes',
    'quorum',
    'razzmatazz',
    'rhubarb',
    'rhythm',
    'rickshaw',
    'schnapps',
    'scratch',
    'shiv',
    'snazzy',
    'sphinx',
    'spritz',
    'squawk',
    'staff',
    'strength',
    'strengths',
    'stretch',
    'stronghold',
    'stymied',
    'subway',
    'swivel',
    'syndrome',
    'thriftless',
    'thumbscrew',
    'topaz',
    'transcript',
    'transgress',
    'transplant',
    'triphthong',
    'twelfth',
    'twelfths',
    'unknown',
    'unworthy',
    'unzip',
    'uptown',
    'vaporize',
    'vixen',
    'vodka',
    'voodoo',
    'vortex',
    'voyeurism',
    'walkway',
    'waltz',
    'wave',
    'wavy',
    'waxy',
    'wellspring',
    'wheezy',
    'whiskey',
    'whizzing',
    'whomever',
    'wimpy',
    'witchcraft',
    'wizard',
    'woozy',
    'wristwatch',
    'wyvern',
    'xylophone',
    'yachtsman',
    'yippee',
    'yoked',
    'youthful',
    'yummy',
    'zephyr',
    'zigzag',
    'zigzagging',
    'zilch',
    'zipper',
    'zodiac',
    'zombie',
]

sad = r'''
██████╗  █████╗ ███╗   ██╗████████╗███████╗██╗  ██╗     ██████╗ ███████╗███████╗██╗ ██████╗██╗ █████╗ ██╗         
██╔══██╗██╔══██╗████╗  ██║╚══██╔══╝██╔════╝╚██╗██╔╝    ██╔═══██╗██╔════╝██╔════╝██║██╔════╝██║██╔══██╗██║         
██║  ██║███████║██╔██╗ ██║   ██║   █████╗   ╚███╔╝     ██║   ██║█████╗  █████╗  ██║██║     ██║███████║██║         
██║  ██║██╔══██║██║╚██╗██║   ██║   ██╔══╝   ██╔██╗     ██║   ██║██╔══╝  ██╔══╝  ██║██║     ██║██╔══██║██║         
██████╔╝██║  ██║██║ ╚████║   ██║   ███████╗██╔╝ ██╗    ╚██████╔╝██║     ██║     ██║╚██████╗██║██║  ██║███████╗    
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝     ╚═════╝ ╚═╝     ╚═╝     ╚═╝ ╚═════╝╚═╝╚═╝  ╚═╝╚══════╝    
██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗     ██████╗  █████╗ ███╗   ███╗███████╗          
██║  ██║██╔══██╗████╗  ██║██╔════╝ ████╗ ████║██╔══██╗████╗  ██║    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝          
███████║███████║██╔██╗ ██║██║  ███╗██╔████╔██║███████║██╔██╗ ██║    ██║  ███╗███████║██╔████╔██║█████╗            
██╔══██║██╔══██║██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║    ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝            
██║  ██║██║  ██║██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗          
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝     ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝          

'''
import random

print(sad)


def game():
    select_word = word_list[random.randint(0, len(word_list))].split(",")
    # print(select_word)
    string_hold = str(select_word[0])
    string_list = []
    string_cipher = []
    for _ in string_hold:
        string_list.append(_)
        string_cipher.append("_")
    string_cipher_hold = ' '.join(string_cipher)
    again = True
    lives = 7
    print(string_hold)
    while lives > 0 and '_' in string_cipher and again:
        print(string_cipher_hold)
        guess = str(input("Guess a letter: ")).lower()
        if not guess.isalpha():
            print(f"{guess} is an INVALID INPUT, please try again")
        elif len(guess) > 1:
            print(f"You guessed {len(guess)} letters at once, please guess just a letter")
        elif guess not in string_hold and lives == 1:
            lives = lives - 1
            print(stages[lives])
        elif guess not in string_hold:
            lives = lives - 1
            print(stages[lives])
            print("WRONG!!!, GUESS AGAIN")
        if lives == 0:
            print("GAME OVER, YOU WERE HANGED")
            ask = input("DO YOU WANT TO PLAY AGAIN Y or N: ").lower()
            if ask == "y":
                game()
            else:
                pass
        if guess in string_cipher:
            print(f"{guess} has already been guessed, Try another letter")
        for _ in range(0, len(string_list)):
            if guess == string_list[_]:
                string_cipher[_] = guess
                string_cipher_hold = ' '.join(string_cipher)

        if '_' not in string_cipher:
            print("CONGRATULATIONS YOU HAVE WON")
            print(f"The final word is {(''.join(string_cipher)).upper()} and you finished with {lives} chances left")
            ask = input("DO YOU WANT TO PLAY AGAIN Y or N: ").lower()
            if ask == "y":
                game()
            else:
                pass


game()
