import random
import time


team_1_score = 0
team_2_score = 0
winner = ""

while True:
    wait_time = random.randint(6,10)
    time.sleep(wait_time)
    
    goal_winner = random.randint(1,2)
    
    if goal_winner == 1:
        team_1_score = team_1_score + 1
        
    if goal_winner == 2:
        team_2_score = team_2_score + 1
    
    print(f"TEAM A: {team_1_score}, TEAM B: {team_2_score}")
        
    if team_1_score == 5:
        winner = "Team A"
        break
    
    if team_2_score == 5:
        winner = "Team B"
        break
    

print(f"The winner is {winner}")

    
      
    
    
    
  