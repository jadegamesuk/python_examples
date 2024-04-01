import random
"""Rock Paper Scissors - No GUI"""

w_l_d = [0, 0, 0]

options = ['rock', 'paper', 'scissors']

print("Play ROCK, PAPER, SCISSORS with the computer")
#print(f"{w_l_d[0]} wins, {w_l_d[1]} lose, {w_l_d[2]} draws ")

def rps_play(user):
    cpu_user = random.choice(options)

    if user == 'r':
        if cpu_user == 'rock':
            w_l_d[2] += 1
            print("DRAW")
        if cpu_user == 'paper':
            w_l_d[1] += 1
            print("LOSE")
        if cpu_user == 'scissors':
            print("WIN")
            w_l_d[0] += 1
    elif user == 'p':
        if cpu_user == 'rock':
            w_l_d[0] += 1
            print("WIN")
        if cpu_user == 'paper':
            w_l_d[2] += 1
            print("DRAW")
        if cpu_user == 'scissors':
            w_l_d[1] += 1
            print("DRAW")
    elif user == 's':
        if cpu_user == 'rock':
            w_l_d[1] += 1
            print("LOSE")
        if cpu_user == 'paper':
            w_l_d[0] += 1
            print("WIN")
        if cpu_user == 'scissors':
            w_l_d[2] += 1
            print("DRAW")
    else:
        print("\nInvalid Input")

while True:

    print(f"\t{w_l_d[0]} wins, {w_l_d[1]} lose, {w_l_d[2]} draws ")
    user_choice = input("\nselect (r)ock, (p)aper or (s)cissors or (q)uit the game ")
    
    if user_choice == 'q':
        print(f"\t{w_l_d[0]} wins, {w_l_d[1]} lose, {w_l_d[2]} draws ")
        break
    else:
        rps_play(user_choice)
    
    
