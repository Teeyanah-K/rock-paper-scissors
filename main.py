import random


while True:
    options = ['R', 'P', 'S']
    computer = random.choice(options)
    player = input("Enter move:")

    while player not in options:
        print('Invalid input!')
        player = input("Pick an option from R, P and S:")

    print(f"The computer plays: {computer}")

    while player == computer:
        print("It's a tie!")
        player = input("Pick an option from R, P and S:")

    if player == "R":
        if computer == "P":
            print("Computer wins :( ")
        else:
            print("Player wins!")
    elif player == "P":
        if computer == "R":
            print("Player win!")
        else:
            print("Computer wins!")
    elif (player == "S"):
        if (computer == "R"):
            print("Computer wins!")
        else:
            print("You win!")
    break
    