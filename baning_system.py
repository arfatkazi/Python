def show_banking_program():
    print("*******************")
    print("  Banking Program   ")
    print("*******************")
    print()
    print("1.Show Balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")




def show_balance(balance):
    print("*******************")
    print(f"Your balance is ₹{balance:2f}")
    print("*******************")
    print()

def deposit():
    amount = float(input("Enter a deposit amount: "))
    
    if amount <0:
        print("*******************")
        print("this is not a valid amount")
        print("*******************")
        print()
        return 0
    else: 
        return amount

def withdraw(balance):
    amount = float(input("Enter amount to be withdrawn: : "))

    if amount > balance:
        print("*******************")
        print("Insufficient funds.")
        print("*******************")
        print()
        return 0
    elif amount < 0:
        print("amount must be greater than 0.")
        return 0

    else:
        return amount



def main():
    balance = 0
    is_running = True


    while is_running:
        show_banking_program()
        choice = input("Enter your choice (1-4): ")
        print()

        if choice == "1":
         show_balance(balance)
        elif choice == "2":
         balance+= deposit()
        elif choice == "3":
         balance-= withdraw(balance)
        elif choice == "4":
            is_running = False
        else:
            print("That is not a valid choice!")
            print()

print("Thank you! Have a nice day!")


if __name__ == '__main__':
   main()