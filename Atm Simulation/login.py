from atm_menu import atm_menu

def login(accounts):
    acc_no = input("Enter Account Number: ")
    pin = input("Enter PIN: ")

    if acc_no in accounts and accounts[acc_no]["pin"] == pin:
        print(f"Welcome {accounts[acc_no]['name']}!")
        atm_menu(accounts, acc_no)   # ✅ pass current_user here
    else:
        print("Invalid Account Number or PIN!")