from withdraw import withdraw
from check_balance import check_balance
def atm():
    while True:
        print("1. Withdraw Money")
        print("2. Check Balance")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            withdraw()
        
        elif choice == "2":
            check_balance()
        
        elif choice == "3":
            print("Thank you for using ATM!")
            break

        else:
            print("Invalid choice!")
atm()