"""
Problem 3

In the famous Rock Paper Scissor game - Rock wins against scissors, paper wins
against rock, and scissors wins against paper.
Write a python program that takes two user inputs and returns who wins the game.
Sample Input:
> Player 1: rock
> Player 2: paper
Sample Output:
> Player 2 is the winner

"""

player1 = input("Player 1: ")
player2 = input("Player 2: ")

if player1 == "rock" and player2 == "scissors":
     print("player 1 is the winner")
if player2 == "rock" and player1 == "scissors":
     print("player 2 is the winner")

if player1 == "paper" and player2 == "rock":
     print("player 1 is the winner")
if player2 == "paper" and player1 == "rock":
     print("player 2 is the winner")

if player1 == "scissors" and player2 == "paper":
     print("player 1 is the winner")
if player2 == "scissors" and player1 == "paper":
     print("player 2 is the winner")

if player1 == player2: print("Tie")
