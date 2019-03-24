"""
AUTHOR:     ERYL KENN VICTORINO
PURPOSE:    ASSIGNMENT 10
            from "Open Source Programming in Python" Course
            with Professor Ivy Liu
MOD DATE:   3/24/2019
"""

"""
1.  Write a program to simulate a game of Rock, Paper, Scissors between two players (the user
    and the computer) and display the outcome (list both players’ choices and who is the winner).
    Assume the computer randomly makes its choices. (Rules: Paper beats Rock – Paper can
    cover Rock, Scissors beat Paper – Scissors can cut Paper, and Rock beats Scissors – Rock
    can break Scissors.)
    *** The program should allow a user to play continuously until she/he choose to quit (an
    option for selection).
"""
import random

# this main function calls play function
def main():
    gameDict = intro()
    pscore, games = play(gameDict)
    totalOutcome(pscore, games)

# game introduction
def intro():
    print("Welcome to Kenn's Rock, Paper, Scissors Simulator!")
    print("Please choose one of the following (number or word):")
    print("1. rock")
    print("2. paper")
    print("3. scissors")
    print("4. quit")
    print()
    numberChoice = ('1', '2', '3', '4')
    wordChoice = ("rock", "paper", "scissors", "quit")
    gameDict = {}

    # making a dictionary gives them the option of using numbers instead of typing the word
    for i in range(len(numberChoice)):
        gameDict[numberChoice[i]] = wordChoice[i]
        gameDict[wordChoice[i]] = numberChoice[i]
    return gameDict
    
# this function loops until the user inputs one of the acceptable choices and returns that choice
def playerChoice(gameDict):
    player = ''
    while player not in (gameDict):
        player not in tuple(gameDict.values())
        player = input("choice:").lower()    
    if player.isnumeric():
        player = gameDict[player]
    return player

# this function randomly chooses a choice for the computer and returns it
def computerChoice():
    choices = ("rock", "paper", "scissors")
    computer = random.choice(choices)
    return computer

# this function determines the outcome based on the choices of the player and the computer and returns
def getResult(player, computer):
    if player == computer:
        return "Draw! Try again."
    elif player == "rock":
        if computer == "scissors":
            return "Player Wins!"
        elif computer == "paper":
            return "Computer Wins!"
    elif player == "paper":
        if computer == "rock":
            return "Player Wins!"
        elif computer == "scissors":
            return "Computer Wins!"
    elif player == "scissors":
        if computer == "paper":
            return "Player Wins!"
        elif computer == "rock":
            return "Computer Wins!"

# this prints out the choices and outcome
def trialOutcome(player, computer, result):
    if player != "quit":
        print("The player chose", player+".")
        print("The computer chose", computer+".")
        print(result)

# this function loops to keep playing the game until the player chooses "quit"
def play(gameDict):
    player = ''
    pscore = 0
    games = 0
    while player != "quit":
        print("Trial", games+1)
        player = playerChoice(gameDict)
        computer = computerChoice()
        result = getResult(player, computer)
        trialOutcome(player, computer, result)
        if result == "Player Wins!":
            pscore += 1
            games += 1
            print()
        elif result == "Computer Wins!":
            games += 1
            print()
    return pscore, games

# this shows to total outcome of all the games played before quitting
def totalOutcome(pscore, games):
    if (pscore or games) != 0:
        print("You won", pscore, "out of", games, "games!")
        print("Your win rate was", "{0:.2%}".format(pscore/games))
    print("Have a nice day!")

main()