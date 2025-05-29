
import random

def spin_row():
    symbols = ['🎈' ,'🎆' ,'🎇' ,'🧨' ,'🎉' ,'🎊']


   

    return [ random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("*******************")
    print("  |  ".join(row))
    print("*******************")
    print()

def get_payout(row,bet):
    if row[0] == row[1] == row[2]:
        return bet * 5
    elif row[0] == row[1] or row[1] == row[2] or row[0] == row[2]:
        return bet * 2
    else:
        return 0



def main():
    current_balance = 100

    print("*********************")
    print("Welcome to Python Slots")
    print("Symbols: 🎈 🎆 🎇 🧨 🎉 🎊")
    print("*********************")
    print()

    while current_balance > 0:
        print("*********************")
        print(f"Current balance ₹{current_balance}")
        print("*********************")
        print()

        bet = input("Place your bet amount: ")

        if  not bet.isdigit():
            print("Please enter a valid number!")
            continue
        
        bet = int(bet)

        if bet > current_balance :
            print("Insuffcient funds.")
            continue


        if bet <= 0:
            print("Bet must be greater than 0")
            continue

        current_balance -=bet

        row =  spin_row()
        print("Spinning....\n")
        print_row(row)

        payout = get_payout(row,bet)
        print(payout)

        if payout > 0:
            print(f"You won ₹{payout}!\n")
        else:
            print("No match. Better luck next time!\n")

        current_balance += payout

        play_again = input("Do you want to play again? (Y/N): ")

        if play_again.upper() != 'Y':
            break

    print("Game over! You're out of money.")
    print()
    print("***********************************")
    print(f"Your final balance is ₹{current_balance}")
    print("***********************************")

if __name__ == '__main__':
    main()