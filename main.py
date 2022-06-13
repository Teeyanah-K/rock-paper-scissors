import random
options = ['R', 'P', 'S']
print("Let's play Rock, Paper, Scissors...\n 'R' for Rock\n 'P' for Paper\n 'S' for Scissors.")

rand = random.choice(options)
Player = input("input R,P or S: ")
R = "rock"
P = "paper"
S = "paper"

print("CPU:", rand)
print("Player:", Player)

Player = input("input R,P or S: ")
while Player not in options:
    while rand != Player:
        if rand == R and Player == S:
            print("CPU wins")
        elif rand == R and Player == P:
            print("You won!")
        elif rand == P and Player == R:
            print("CPU wins")
        elif rand == P and Player == S:
            print("You won!")
        elif rand == S and Player == P:
            print("CPU wins")
        elif:
            print("You won!")
        else:
            print("It's a tie. Try again!")   
    print("Error! Invalid Input")
