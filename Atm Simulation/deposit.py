def deposit(accounts, current_user):
    amount = int(input("Enter amount to deposit: ₹"))

    if amount <= 0:
        print("Invalid amount!")
    else:
        accounts[current_user]['balance'] += amount
        accounts[current_user]['transactions'].append(f"Deposited ₹{amount}")
        print("Deposit successful!")