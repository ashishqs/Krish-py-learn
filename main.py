counter = 0

choice = ''


while True:
    choice = input( f"Your options are c = imcrease counter, r = reset counter, and q= stop counter: " )
    
    if choice == "c":
        counter = counter + 1
        
    if choice == "s":
        print("REVEALING YOUR SCORE: ", counter)
    
    if choice == "r":
        counter = 0
    
    
    if choice == "q":
        break

print(f"Your score is {counter}")
    
    
    
    
 
    
    
    
