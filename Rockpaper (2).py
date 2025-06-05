#Anyla Reeves
#1/10/25

#init
import random
wins = 0 #Tracks players wins
losses = 0 #Tracks players losses
ties = 0 #Tracks players ties
#function
#main
def rpsgame():
    global wins
    global losses
    global ties
    while True: #looping a code
        print("welcome to rock paper scissor") #Welcome player to the game
        #step 1: collect player move
        print("Make your move") # asking player for their move
        player=input("rock, paper, scissors, go:")# input player can put in
        player = random.randint(1,3) # randomizing what the comuter is gonna pick for its input
        if player == 1:
            player = "rock"
            print("The player move is rock!") #

        if player == 2:
            player = "paper"
            print("The player move is paper")

        if player == 3:
            player = "scissor"
            print("The player move is scissor")

        #step 2: Generate a move for the computer
        computer=random.randint(1,3)
        if computer == 1:
            computer = "rock"
            print("The computer's move is rock!")

        if computer == 2:
            computer = "paper"
            print("The computer's move is paper!")

        if computer == 3:
            computer = "scissor"
            print("The computer's move is scissor!")

        #step 3: determine the outcome

        print("the result is...")

        if player == "rock" and computer == "rock":
            print("it is a tie!")
            ties = ties + 1
        elif player == "rock" and computer == "paper":
            print("you lose")
            losses = losses + 1
        if player == "scissor" and computer == "paper":
            print("you win!")
            wins = wins + 1
        elif player == "paper" and computer == "paper":
            print("it is a tie!")
            ties = ties + 1
        if player == "scissors" and computer == "rock":
            print("you lose")
            losses = losses + 1
        if player == "paper" and computer == "scissors":
            print("the result is, computer win")
            losses = losses + 1
        if player == "rock" and computer == "scissor":
            print("player win")
            wins = wins + 1
        if player == "scissor" and computer == "scissor":
            print("it's a tie")
            ties = ties + 1


        #step 4: loop the program until player wants to stop
        playagain = input("would you like to playr again ")
        if playagain.lower() == "yes":
            print("restarting...")
        else:
            print("Thanks for playing")
            break
        #step 5: keep track of win and losses

#Main
rpsgame()



