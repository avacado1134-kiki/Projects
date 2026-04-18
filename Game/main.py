from decision import decide_winner
from computer_choice import get_computer_choice
from user_choice import get_user_choice

def play_game():
    while True:
        user = get_user_choice()
        if user is 0:
            continue  
         
        computer = get_computer_choice()
        
        print("You chose:", user)
        print("Computer chose:", computer)
        print(decide_winner(user, computer))
        
        again = input("Do you want to play again? (yes/no): ").lower()
        if again != "yes":
            print("Thanks for playing!")
            break

       
play_game()