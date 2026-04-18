def withdraw(accounts, current_user):
    amount = int(input("Enter amount to withdraw: ₹"))

    if amount <= 0:
        print("Invalid amount!")
    elif amount > accounts[current_user]['balance']:
        print("Insufficient balance!")
    else:
        accounts[current_user]['balance'] -= amount
        accounts[current_user]['transactions'].append(f"Withdrew ₹{amount}")
        print("Withdrawal successful!")