def show_balance(balance):
    print("XXXXXXXXXXXXXXXXXXXX")
    print(f"Your balance is {balance:.2f}")
    print("XXXXXXXXXXXXXXXXXXXXXX")


def deposit():
    amount = float(input("Enter an amount to be deposited: "))
    if amount < 0:
        print("That's not a valid amount")
        return 0
    else:
        return amount


def withdraw(balance):
    amount = float(input('Enter amount to be withdrawn: '))
    if amount > balance:
        print('Insufficient funds')
        return 0
    elif amount < 0:
        print("XXXXXXXXXXXXXXX")
        print("Amount must be greater than 0")
        print("XXXXXXXXXXXXXXX")
        return 0
    else:
        return amount


def main():
    balance = 0
    is_running = True

    while is_running:
        print("XXXXXXXXXXXXXXXXX")
        print("Banking Program")
        print("XXXXXXXXXXXXXXXXX")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("XXXXXXXXXXXXXXXXXXX")
        choice = input("Enter your choice (1->4):")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print("XXXXXXXXXXXXXX")
            print("This is not a valid choice")
            print("XXXXXXXXXXXXXX")

    print("Thank you! Have a nice day")


if __name__ == '__main__':
    main()
