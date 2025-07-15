import random
import time
import pygame
import math

# Initialize pygame mixer for sound effects
pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512)
pygame.mixer.init()

def create_wave_sound(frequency, duration, amplitude=0.3, sample_rate=44100):
    """Create a sine wave sound"""
    frames = int(duration * sample_rate)
    arr = []
    
    for i in range(frames):
        wave = amplitude * math.sin(2 * math.pi * frequency * i / sample_rate)
        # Create stereo sound
        sample = int(wave * 32767)
        arr.extend([sample, sample])  # left and right channels
    
    # Convert to pygame sound
    sound_array = pygame.array.array('h', arr)
    return pygame.sndarray.make_sound(sound_array)

def play_goal_sound():
    """Play exciting goal sound effect with multiple tones"""
    print("🎵 *EPIC GOAL SOUND* 🎵")
    
    # Play ascending notes for excitement
    frequencies = [440, 554, 659, 880]  # A, C#, E, A (A major chord)
    for freq in frequencies:
        sound = create_wave_sound(freq, 0.3, amplitude=0.4)
        sound.play()
        time.sleep(0.2)

def play_crowd_cheer():
    """Simulate crowd cheering with rumbling sound"""
    print("👏 *CROWD ROARING* 👏")
    
    # Create a crowd rumble effect with low frequency
    rumble = create_wave_sound(120, 1.0, amplitude=0.3)
    rumble.play()

def play_winner_fanfare():
    """Play victory fanfare"""
    print("🎺 *VICTORY CELEBRATION* 🎺")
    
    # Play "Charge!" melody - a classic sports fanfare
    melody = [
        (523, 0.4),  # C
        (523, 0.4),  # C
        (523, 0.4),  # C
        (659, 0.8),  # E
    ]
    
    for freq, duration in melody:
        sound = create_wave_sound(freq, duration, amplitude=0.5)
        sound.play()
        time.sleep(duration + 0.1)

def play_whistle():
    """Play referee whistle sound"""
    print("🔔 *WHISTLE* 🔔")
    whistle = create_wave_sound(2000, 0.5, amplitude=0.3)
    whistle.play()

# Game variables
team_1_score = 0
team_2_score = 0
winner = ""

print("🏆 SOCCER CHAMPIONSHIP MATCH! 🏆")
print("🔊 Turn up your speakers for the full experience! 🔊")
print("=" * 60)

# Play initial whistle and crowd
play_whistle()
time.sleep(1)
play_crowd_cheer()

while True:
    # Simulate a goal being scored
    wait_time = random.randint(6,10)
    
    # Build anticipation during wait time
    if wait_time > 7:
        print("⏰ Building up to something exciting...")
        time.sleep(wait_time // 2)
        print("🏟️ *Crowd getting louder...* 🏟️")
        play_crowd_cheer()
        time.sleep(wait_time - wait_time // 2)
    else:
        time.sleep(wait_time)
    
    print("\n" + "="*30)
    print("⚽ GOOOOOAAAAL!!! ⚽")
    print("="*30)
    
    # Play epic goal sound effect
    play_goal_sound()
    
    # Randomly determine which team scores
    goal_winner = random.randint(1,2)
    
    # Update the score based on the goal winner
    if goal_winner == 1:
        team_1_score = team_1_score + 1
        print(f"🎯 TEAM A SCORES! 🎯")
        
    if goal_winner == 2:
        team_2_score = team_2_score + 1
        print(f"🎯 TEAM B SCORES! 🎯")
    
    print(f"📊 Current Score: TEAM A: {team_1_score} | TEAM B: {team_2_score}")
    
    # Play celebration cheer
    time.sleep(0.5)
    play_crowd_cheer()
    
    # Check if either team has reached 5 goals
    if team_1_score == 5:
        winner = "Team A"
        break
    
    if team_2_score == 5:
        winner = "Team B"
        break
    
    time.sleep(2)  # Brief pause between goals

# Final whistle
print("\n🔔 *FINAL WHISTLE* 🔔")
play_whistle()
time.sleep(1)

# Winner announcement with fanfare!
print("\n" + "=" * 60)
print("🎉🎉🎉 FULL TIME! GAME OVER! 🎉🎉🎉")
print("=" * 60)
print("📋 FINAL SCORE:")
print(f"🏆 TEAM A: {team_1_score}")
print(f"🏆 TEAM B: {team_2_score}")
print("=" * 60)
print(f"👑 CHAMPIONS: {winner.upper()}! 👑")
print("=" * 60)

# Play epic victory celebration
play_winner_fanfare()
time.sleep(1)
play_crowd_cheer()

print("\n🎊 Thanks for watching the match! 🎊")
print("🔊 Hope you enjoyed the sound effects! 🔊")

# Clean up
pygame.mixer.quit()
