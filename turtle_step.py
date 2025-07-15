import random


def print_turtle_steps(counter):
    if counter <= 0:
        return
    while True:
        print(f"Step {counter}: Turtle takes a step!")
        counter = counter - 1
        
        if counter == 0:
            break
        
def roll_a_dice():
    return random.randint(1, 6)



print_turtle_steps(3)

print("===========================================")
print_turtle_steps(15)
print("===========================================")
print_turtle_steps(20)
print("===========================================")
print_turtle_steps(-100000000)
number=roll_a_dice()

if number == 6:
    print("Congratulations. You won the gambling game!" )
else:
    print(f'You got {number}. Better luck next time.')
