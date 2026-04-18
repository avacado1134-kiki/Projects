from account import accounts
from login import login

while True:
    print("\n===== ATM SYSTEM =====")
    print("1. Login")
    print("2. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        login(accounts)
    elif choice == '2':
        print("Thank you!")
        break
    else:
        print("Invalid choice!")