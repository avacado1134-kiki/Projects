def get_user_choice():
    choice = input("Enter rock, paper, or scissors: ").lower()
    if choice not in ["rock", "paper", "scissors"]:
        print("Invalid input! Please try again.")
        return 0
    return choice
