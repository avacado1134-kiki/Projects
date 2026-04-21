from roll_a_die import roll_dice
from r_p_s import play_game
while True:
    print("---------------Lets Start the Game Play🎮-----------------")
    print("")
    print("Which Game you want to play (Rock🪨, Paper📃, or Scissors✂️ ) or (Roll a Dice🎲)?")
    print("1.Enter 1 for playing Rock,Paper or Scissors:")
    print("2.Enter 2 for playing Rock,Paper or Scissors:")
    print("3.Enter 3 to Exit the Game Play")
    choose=int(input("Enter Your Choice:"))
    if choose==1:
        play_game()
    elif choose==2:
        roll_dice()
    elif choose==3:
        print("Thank You For playing !!")
        break
    else:
        print("Invalid Input,Please Try Again!!")

