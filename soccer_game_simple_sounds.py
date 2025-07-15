import random
import time
import os
import subprocess

def play_sound_effect(sound_type="beep"):
    """Play sound effects using macOS say command and system sounds"""
    try:
        if sound_type == "goal":
            # Use text-to-speech for exciting goal announcement
            subprocess.run(['say', '-v', 'Samantha', '-r', '250', 'GOOOOOOOAAAAL!'], 
                         check=False, capture_output=True)
        elif sound_type == "goal_celebration":
            # Multiple celebration sounds
            subprocess.run(['afplay', '/System/Library/Sounds/Glass.aiff'], 
                         check=False, capture_output=True)
            time.sleep(0.3)
            subprocess.run(['afplay', '/System/Library/Sounds/Ping.aiff'], 
                         check=False, capture_output=True)
        elif sound_type == "cheer":
            # Play system sound for crowd cheer
            subprocess.run(['afplay', '/System/Library/Sounds/Glass.aiff'], 
                         check=False, capture_output=True)
        elif sound_type == "big_cheer":
            # Bigger crowd celebration
            subprocess.run(['afplay', '/System/Library/Sounds/Sosumi.aiff'], 
                         check=False, capture_output=True)
        elif sound_type == "fanfare":
            # Play triumphant sound
            subprocess.run(['afplay', '/System/Library/Sounds/Sosumi.aiff'], 
                         check=False, capture_output=True)
        elif sound_type == "fireworks":
            # Fireworks sound effect
            subprocess.run(['afplay', '/System/Library/Sounds/Blow.aiff'], 
                         check=False, capture_output=True)
        elif sound_type == "whistle":
            # Play whistle sound
            subprocess.run(['afplay', '/System/Library/Sounds/Blow.aiff'], 
                         check=False, capture_output=True)
    except:
        # Fallback to print if sounds don't work
        print(f"🔊 *{sound_type.upper()} SOUND* 🔊")

def play_beep_sound(frequency=1000, duration=0.5):
    """Play a simple beep sound using system beep"""
    # Try multiple approaches for sound
    try:
        # Method 1: Use macOS say command for beep
        subprocess.run(['say', '-v', 'Zarvox', 'beep'], 
                     check=False, capture_output=True, timeout=2)
    except:
        try:
            # Method 2: Use system beep
            os.system('echo -e "\\007"')
        except:
            # Method 3: Print fallback
            print("🔊 *BEEP* 🔊")

def play_goal_sound():
    """Play exciting goal sound effect with full celebration"""
    print("🎵 *EPIC GOAL CELEBRATION* 🎵")
    
    # Step 1: Goal announcement
    play_sound_effect("goal")
    time.sleep(0.8)
    
    # Step 2: Multiple celebration sounds
    play_sound_effect("goal_celebration")
    time.sleep(0.5)
    
    # Step 3: Crowd goes wild
    play_sound_effect("big_cheer")
    time.sleep(0.3)
    
    # Step 4: Commentary excitement
    celebrations = [
        "What a magnificent goal!",
        "Absolutely spectacular!",
        "The crowd goes wild!",
        "Incredible technique!",
        "Pure magic on the field!"
    ]
    comment = random.choice(celebrations)
    subprocess.run(['say', '-v', 'Daniel', '-r', '180', comment], 
                 check=False, capture_output=True)

def play_crowd_cheer():
    """Simulate crowd cheering"""
    print("👏 *CROWD CHEERING* 👏")
    play_sound_effect("cheer")

def play_fireworks_show():
    """Play an epic fireworks show for the winner"""
    print("\n🎆🎆🎆 FIREWORKS SPECTACULAR! 🎆🎆🎆")
    
    # Multiple fireworks bursts
    for i in range(5):
        print(f"💥 BOOM! Firework #{i+1} 💥")
        play_sound_effect("fireworks")
        time.sleep(0.4)
        
        # Add sparkle sounds
        subprocess.run(['afplay', '/System/Library/Sounds/Ping.aiff'], 
                     check=False, capture_output=True)
        time.sleep(0.3)
    
    print("✨✨✨ GRAND FINALE! ✨✨✨")
    # Grand finale with multiple sounds
    subprocess.run(['afplay', '/System/Library/Sounds/Sosumi.aiff'], 
                 check=False, capture_output=True)
    time.sleep(0.5)
    subprocess.run(['afplay', '/System/Library/Sounds/Glass.aiff'], 
                 check=False, capture_output=True)

def play_winner_fanfare():
    """Play victory fanfare for the winner with epic celebration"""
    print("🎺 *CHAMPIONSHIP CELEBRATION* 🎺")
    
    # Step 1: Victory fanfare
    play_sound_effect("fanfare")
    time.sleep(1)
    
    # Step 2: Victory speech
    victory_speeches = [
        "Ladies and gentlemen, we have our champions!",
        "What an absolutely incredible match!",
        "The crowd is on their feet!",
        "History has been made today!"
    ]
    speech = random.choice(victory_speeches)
    subprocess.run(['say', '-v', 'Samantha', '-r', '160', speech], 
                 check=False, capture_output=True)
    
    time.sleep(0.5)
    
    # Step 3: Final celebration announcement
    subprocess.run(['say', '-v', 'Daniel', '-r', '140', 'Congratulations to the champions! Let the celebration begin!'], 
                 check=False, capture_output=True)

# Game variables
team_1_score = 0
team_2_score = 0
winner = ""

print("🏆 SOCCER CHAMPIONSHIP MATCH! 🏆")
print("Listen for the exciting sound effects!")
print("=" * 50)

# Play initial crowd cheer
play_crowd_cheer()

while True:
    # Simulate a goal being scored
    wait_time = random.randint(6,10)
    
    # Show anticipation during wait time
    if wait_time > 7:
        time.sleep(wait_time // 2)
        print("🏟️ *Crowd getting excited...* 🏟️")
        play_crowd_cheer()
        time.sleep(wait_time - wait_time // 2)
    else:
        time.sleep(wait_time)
    
    print("⚽ GOAL!!! ⚽")
    
    # Play epic goal celebration
    play_goal_sound()
    
    # Randomly determine which team scores
    # 1 for Team A, 2 for Team B
    goal_winner = random.randint(1,2)
    
    # Update the score based on the goal winner
    if goal_winner == 1:
        team_1_score = team_1_score + 1
        print(f"\n🎯 ⭐ TEAM A SCORES! ⭐ 🎯")
        print(f"🏟️ Stadium erupts as Team A takes it to {team_1_score}!")
        
    if goal_winner == 2:
        team_2_score = team_2_score + 1
        print(f"\n🎯 ⭐ TEAM B SCORES! ⭐ 🎯")
        print(f"🏟️ Stadium erupts as Team B takes it to {team_2_score}!")
    
    print(f"📊 SCOREBOARD: TEAM A: {team_1_score} | TEAM B: {team_2_score}")
    
    # Extended celebration based on score
    if team_1_score >= 3 or team_2_score >= 3:
        print("🔥 This is getting intense! The crowd is going crazy! 🔥")
        play_sound_effect("big_cheer")
        time.sleep(0.5)
    
    # Play celebration cheer
    play_crowd_cheer()
    
    # Check if either team has reached 5 goals
    if team_1_score == 5:
        winner = "Team A"
        break
    
    if team_2_score == 5:
        winner = "Team B"
        break
    
    time.sleep(1)  # Brief pause between goals

# Winner announcement with EPIC celebration!
print("\n" + "🎉" * 25)
print("�🏆🏆 CHAMPIONSHIP FINALE! 🏆🏆🏆")
print("🎉" * 25)
print("\n📢 FINAL WHISTLE! THE MATCH IS OVER! 📢")
print("=" * 60)
print("📋 OFFICIAL FINAL SCORE:")
print(f"🥅 TEAM A: {team_1_score} goals")
print(f"🥅 TEAM B: {team_2_score} goals")
print("=" * 60)
print(f"👑🏆 CHAMPIONS: {winner.upper()}! 🏆👑")
print("=" * 60)

# Epic championship celebration sequence
print("\n🎪 CHAMPIONSHIP CELEBRATION BEGINS! 🎪")

# Play victory fanfare with commentary
play_winner_fanfare()
time.sleep(1)

# FIREWORKS SHOW!
play_fireworks_show()
time.sleep(1)

# Final crowd celebration
print("\n🏟️ The entire stadium is on their feet! 🏟️")
play_sound_effect("big_cheer")
time.sleep(0.5)

# Victory lap announcement
subprocess.run(['say', '-v', 'Samantha', '-r', '150', f'{winner} takes their victory lap around the stadium!'], 
             check=False, capture_output=True)

print(f"\n🎊🎊🎊 {winner.upper()} TAKES THE TROPHY! 🎊🎊🎊")
print("🏆 What an absolutely magnificent match! 🏆")

print("\n✨ Thanks for watching this epic championship! ✨")
print("🎮 Hope you enjoyed the spectacular sound effects! �")
