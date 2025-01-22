import random

# Partner Wrote
red = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 29, 31, 33, 35]
black = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]
names = []


def roulette_number():
    number = red + black

    return random.choice(number)
# End Citation

def deposit_money():
    while True:
        player_name = input("What is your name? ").strip()
        if not player_name:
            print("Please enter a valid name.")
            continue
# ChatGPT Citation
        try:
            player_bank = int(input("Please enter the amount you're depositing: "))
            if player_bank <= 0:
                print("Please deposit a positive amount.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer for the deposit.")

    print(f"You have ${player_bank} in your bank.")
    names.append(player_name)
    return player_bank, player_name


def betting(player_bank):
    while True:
        try:
            betting_amount = int(input("How much would you like to bet? "))
            if betting_amount <= 0:
                print("Sorry, you can't bet less than zero.")
                continue
            elif betting_amount > player_bank:
                print(f"Please enter a valid betting amount. You only have ${player_bank} in your bank.")
            else:
                player_bank -= betting_amount
                print(f"You have ${player_bank} in your bank and you are betting ${betting_amount}")
                return betting_amount, player_bank
        except ValueError:
            print("Please enter a valid number.")
#End Citation

def switch_player():
    while len(names) < 8:
        response = input("Would you like to add another player (Max 8)? y/n ").strip().lower()
        if response == 'y':
            print("Adding another player...")
            deposit_money()
        elif response == 'n':
            print("No more players will be added.")
            break
        else:
            print("Invalid input, please enter 'y' or 'n'.")

# Partner Wrote
def roulette_game():
    while True:

        response = input("Red or Black? ")
        if response == "Red":
            print(red)
            red_choice = input("Please choose a number out of the above: ")
            # ChatGPT: Debug following roulette game code:
            if red_choice.isdigit() and int(red_choice) in red:
                roulette_number(red, black)
            # End citation
            else:
                print("Please choose a number within the list given: ")
        elif response == "Black":
            print(black)
            black_choice = input("Please choose a number out of the above: ")
            if black_choice.isdigit() and int(black_choice) in black:
                roulette_number(red, black)
            else:
                print("Please choose a number within the list given: ")
        else:
            print("Invalid input, please enter either 'Red' or 'Black'.")


# End Citation

def store_names():
    players = []
    try:
        num_players = int(input("Enter the number of players "))
    except ValueError:
        print("Please enter a valid number")
        return
#ChatGPT citation
    for i in range(num_players):
        while True:
            name = input(f"Enter name for player {i + 1}: ").strip()
            if not name:
                print("Name cannot be empty. Please enter a valid name.")
            elif name in players:
                print(f"Name '{name}' is already taken. Please choose a different name.")
            else:
                players.append(name)
                break

    print("Players:", players)
    return players

player_bank, player_name = deposit_money()
betting_amount, player_bank = betting(player_bank)
roulette_game()
roulette_number()
switch_player()
#End Citation