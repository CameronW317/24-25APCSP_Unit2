import random

def print_rules():
    print("Welcome to American Roulette!")
    print("In American Roulette, the wheel has 38 slots: numbers 1-36, plus 0 and 00.")
    print("You can bet on a specific number, a color (red or black), or odd/even.")
    print("Payouts:")
    print("  - Bet on a number: 35:1")
    print("  - Bet on red/black or odd/even: 1:1")
    print("Good luck!\n")

def deposit_money():
    while True:
        try:
            player_bank = int(input("Please enter the amount you're depositing: $"))
            if player_bank <= 0:
                print("Please deposit a positive amount.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer for the deposit.")
    return player_bank

def betting(player_bank):
    while True:
        print(f"\nYou have ${player_bank} in your bank.")
        bet_type = input("What would you like to bet on? (number/color/odd/even): ").lower()

        if bet_type == "number":
            try:
                bet_number = int(input("Choose a number between 0 and 36 to bet on: "))
                if bet_number < 0 or bet_number > 36:
                    print("Invalid number. Please choose a number between 0 and 36.")
                    continue
            except ValueError:
                print("Please enter a valid number.")
                continue
        elif bet_type in ["color", "odd", "even"]:
            bet_number = None
        else:
            print("Invalid bet type. Please choose 'number', 'color', or 'odd/even'.")
            continue

        while True:
            try:
                betting_amount = int(input(f"How much would you like to bet on {bet_type}? $"))
                if betting_amount <= 0:
                    print("Betting amount must be greater than 0.")
                    continue
                if betting_amount > player_bank:
                    print(f"You don't have enough money. You have ${player_bank}.")
                    continue
                break
            except ValueError:
                print("Please enter a valid amount.")

        player_bank -= betting_amount
        return bet_type, bet_number, betting_amount, player_bank

def spin_wheel():
    # 38 numbers: 0, 00, and 1 to 36
    wheel = [0, "00"] + list(range(1, 37))
    return random.choice(wheel)

def check_win(bet_type, bet_number, result, betting_amount):
    if bet_type == "number" and result == bet_number:
        print(f"Congratulations! The ball landed on {result}. You win ${betting_amount * 35}.")
        return betting_amount * 35
    elif bet_type == "color":
        # 18 red numbers and 18 black numbers
        red_numbers = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
        black_numbers = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
        if result in red_numbers and bet_number == "red":
            print(f"Congratulations! The ball landed on {result}. You win ${betting_amount}.")
            return betting_amount
        elif result in black_numbers and bet_number == "black":
            print(f"Congratulations! The ball landed on {result}. You win ${betting_amount}.")
            return betting_amount
        else:
            print(f"The ball landed on {result}. You lose your bet.")
            return -betting_amount
    elif bet_type == "odd" and isinstance(result, int) and result % 2 != 0:
        print(f"Congratulations! The ball landed on {result}. You win ${betting_amount}.")
        return betting_amount
    elif bet_type == "even" and isinstance(result, int) and result % 2 == 0:
        print(f"Congratulations! The ball landed on {result}. You win ${betting_amount}.")
        return betting_amount
    else:
        print(f"The ball landed on {result}. You lose your bet.")
        return -betting_amount

def play_game():
    print_rules()
    player_bank = deposit_money()

    while player_bank > 0:
        bet_type, bet_number, betting_amount, player_bank = betting(player_bank)
        result = spin_wheel()
        print(f"\nThe ball landed on {result}.")
        winnings = check_win(bet_type, bet_number, result, betting_amount)
        player_bank += winnings
        print(f"Your new balance is ${player_bank}.")

        if player_bank <= 0:
            print("You have run out of money. Game over.")
            break

        play_again = input("\nWould you like to play again? (y/n): ").lower()
        if play_again != "y":
            print("Thanks for playing! Your final balance is ${}".format(player_bank))
            break

if __name__ == "__main__":
    play_game()
