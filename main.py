from random import randint

#created list to store all possible options; Rock, Papper or Scissors
my_list = ["Rock", "Paper", "Scissors"]

#assigning a random play to the computer
computer = my_list[randint(0,2)]

#setting player to False
player = False

while player == False:
#setting player to True
    player = input("Please pick either Rock, Paper or Scissors ?")
    if player == computer:
        print("Tie! The computer and player pick the same move")
    elif player == "Rock":
        if computer == "Paper":
            print(f"Computer chooses {computer}...")
            print("You lose!", computer, "covers", player)
        else:
            print(f"Computer chooses {computer}...")
            print("You win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print(f"Computer chooses {computer}...")
            print("You lose!", computer, "cut", player)
        else:
            print(f"Computer chooses {computer}...")
            print("You win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print(f"Computer chooses {computer}...")
            print("You lose...", computer, "smashes", player)
        else:
            print(f"Computer chooses {computer}...")
            print("You win!", player, "cut", computer)
    else:
        print("That's not a valid play. Check your spelling! or letter case")
    #player was set to True, but we want it to be False so the loop continues
    player = False
    computer = my_list[randint(0,2)]
