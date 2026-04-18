def show_statement(accounts, current_user):
    print("\n--- Statement ---")
    txns = accounts[current_user]['transactions']

    if not txns:
        print("No transactions yet.")
    else:
        for t in txns:
            print(t)