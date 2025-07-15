import random

chance = 0
number = random.randint(1,20)
game_ended = False

while True:
    
    guess_str = input("What is your guess?  ")
    guess = int(guess_str)
    chance = chance + 1

    if guess < number:
        print("Low")
        
            
    if guess > number:
        print("High")
       
        
    if guess == number:
        print("Congratulations! You win!")
        game_ended = True
    
    
    if chance == 5 and game_ended == False:
        print(f"You lost. The number was {number}")
        game_ended = True
    
    if game_ended == True:
        choice = input("Would you like to play again? (Y/n)   ")
        if choice == "" or choice == "Y":
            number = random.randint(1,20)
            chance = 0
            game_ended = False
        else:
            break
    
        
        
        
        
        
        
        
        
        