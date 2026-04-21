def roll_dice():
    import random
    while True:
        choice=input("Want to roll a dice🎲(yes/no):").lower()
        if choice=="yes":
            print("Lets roll the dice!!")
            print(f"The output of rolling the dice is: {random.randint(1,6)}")
        elif choice=="no":
            print("Game Over")
            break
        else:
            print("Please enter yes or no!!")