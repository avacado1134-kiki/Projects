from check_balance import display_balance
from deposit import deposit
from withdraw import withdraw
from statement import show_statement

def atm_menu(accounts, current_user):
    while True:
        print("\n===== ATM MENU =====")
        print("1. Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Statement")
        print("5. Logout")

        choice = input("Enter choice: ")

        if choice == '1':
            display_balance(accounts, current_user)
        elif choice == '2':
            deposit(accounts, current_user)
        elif choice == '3':
            withdraw(accounts, current_user)
        elif choice == '4':
            show_statement(accounts, current_user)
        elif choice == '5':
            print("Logged out.")
            break
        else:
            print("Invalid choice!")