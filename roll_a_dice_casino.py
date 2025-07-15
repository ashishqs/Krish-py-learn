# Excerise: The purpose of this program is to build a casino business entirely on rolling a dice.
# A player clicks on "play" button (top right corner) to start a playing session.
# When playing session starts, casino's balance is 100$. (Hint: Think of this as variable at the beginning of program)
# Player is required to have 50$ to start the game. (Hint: think of this as another variable at the beginning of program)
# Unlimited plays are allowed until user choose to quit (Hint: in endless while True loop, take user input. If "1" to "6" is entered, game is played with 1$ bet, 'q' will quit the game. Any other option, user will be reminded for valid options and prompted again)
# If user wins the "play" (HINT: if user_choice == dice_number, user's balance increases by 4$)
# If user loses, casino's money increases by 1 (Hint: increase casino balance)
# when program ends (HINT: user chooses 'q'), show Casino balance (HINT: variable) and User's Balance (HINT: variable) 

## Example:
# User starts the program
# 2. user is given options to play or quit
# 3. User choose "1", computer rolls dice and randomly choose 3. User loses 1$, casino gains 1$
# 2. user is given option to play or exit
# User chooses 1, rolls give gives 1, user balance goes up by 3
# user is given options to play or quit, user quits
# computer prints Casino Balance: 98, User balance is 52


import random


print("Welcome Fellow gamblers. I'd like to introduce you to roll a dice and becom a millionaire(only by doing it around 800,000 times.) My name is the Frontman. but call me 456.")
casino_balance = 100
user_balance = 50
while True:
    choice = input("Your choices are: 1,2,3,4,5,6,q (Quit Playing):  ")
    

    if choice not in ["1", "2", "3", "4", "5", "6", "q"]:
        print("Not valid")
        continue
    
    
    number =  random.randint(1, 6)
    print(f"{number}")
     


    
    if choice == str(number):
        user_balance = user_balance + 4
        print(f"Congrats you balance is now {user_balance}")    
    
    else:
        casino_balance = casino_balance + 1
        user_balance = user_balance - 1
        print(f"Sorry for your bank balance. Better luck next time.Your balance is {user_balance}")
    
    
    if choice == "q":
        print(f"USER BALANCE: {user_balance}")
        print(f"CASINO BALANCE: {casino_balance}")
        break
    
    


