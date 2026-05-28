logo = r'''
 _____________________
|  _________________  |
| | Dantex Official    0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |___CALULATOR______________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
'''
print(logo)
# Calculator
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


caculation = \
    {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide
    }


def calculator():
    num1 = float(input("What is the first number: "))

    for operation in caculation:
        print(operation)
    pick = input("Which operation do you want use: ")
    num2 = float(input("What is the second number: "))
    result1 = 0
    for _ in caculation:
        if _ == pick:
            result1 = caculation[_](num1, num2)
    print(f"{num1} {pick} {num2} = {result1}")
    ask = True
    result2 = result1
    while ask:
        temp = 0
        asks = input(f"Do you want to keep calculating with {result2} Yes(Y) or No(N) or Exit(E) to start over: ").lower()
        if asks == "yes" or asks == "y":
            print("Pick an operation")
            for operation in caculation:
                print(operation)
            pick = input("Which operation do you want use: ")
            num3 = float(input("What is the next number: "))
            for _ in caculation:
                if _ == pick:
                    temp = result2
                    result2 = caculation[_](temp, num3)
            print(f"{temp} {pick} {num3} = {result2}")
        elif asks == "no" or asks == "n":
            ask = False
            print(f"Thanks for using, Your final answer is {result2}")
        elif asks == "exit" or asks == "e":
            calculator()
            ask = False

calculator()

