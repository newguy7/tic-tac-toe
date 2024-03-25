# TIC TAC TOE

'''
X O O
X O O
O X X

played between 2 players
one will be user
one will be computer

computer will make turns randomly
first turn will also be decided randomly
you will ask user which icon it wants to use

1|2|3
4|5|6
7|8|9

'''

import random
import pandas as pd

players = ['Computer','User']
icon_choice = ['X','O']
board = []
#game = 1

# decide random turn
def select_turn():
  return random.choice(players)

# display board
def display_board(board):
  print("|" +str(board[0])+ "|" + str(board[1])+ "|" + str(board[2])+ "|")
  print("|" +str(board[3])+ "|" + str(board[4])+ "|" + str(board[5])+ "|")
  print("|" +str(board[6])+ "|" + str(board[7])+ "|" + str(board[8])+ "|")
  print("======================================")

# select icon
def select_icon():
  user_icon = input("Please select your icon(X/O): ").upper()
  while (user_icon not in icon_choice):
    print(f"The icon choices are: {icon_choice}")
    user_icon = input("Please select your icon: ").upper()
  comp_icon = 'X' if user_icon == 'O' else 'O'

  print(f"User's icon: {user_icon}")
  print(f"Computer's icon: {comp_icon}")
  return user_icon, comp_icon

def check_winner(board,turn):
  if board[0] == board[1] and board[1] == board[2] and board[0] != " ":
    print("Game Over!")
    print(f"{turn} won.")
    game = 0
  elif board[3] == board[4] and board[4] == board[5] and board[3] != " ":
    print("Game Over!")
    print(f"{turn} won.")
    game = 0
  elif board[6] == board[7] and board[7] == board[8] and board[6] != " ":
    print("Game Over!")
    print(f"{turn} won.")
    game = 0
  elif board[0] == board[3] and board[3] == board[6] and board[6] != " ":
    print("Game Over!")
    print(f"{turn} won.")
    game = 0
  elif board[1] == board[4] and board[4] == board[7] and board[7] != " ":
    print("Game Over!")
    print(f"{turn} won.")
    game = 0
  elif board[2] == board[5] and board[5] == board[8] and board[8] != " ":
    print("Game Over!")
    print(f"{turn} won.")
    game = 0
  elif board[0] == board[4] and board[4] == board[8] and board[4] != " ":
    print("Game Over!")
    print(f"{turn} won.")
    game = 0
  elif board[2] == board[4] and board[4] == board[6] and board[2] != " ":
    print("Game Over!")
    print(f"{turn} won.")
    game = 0
  elif board[0] != ' ' and board[1] != ' ' and board[2] != ' ' and board[3] != ' ' and board[4] != ' ' and board[5] != ' ' and board[6] != ' ' and board[7] != ' ' and board[8] != ' ':
    print("Game ended as Draw!!")
    game = 0
  else:
    game = 1
  return game

# make the move according to the user's move if applicable
def super_computer(board, user_icon):
  # Horizontal check
  if board[0] == board[1] == user_icon and board[2] == ' ':
    comp_choice = 2
  elif board[1] == board[2] == user_icon and board[0] == ' ':
    comp_choice = 0
  elif board[0] == board[2] == user_icon and board[1] == ' ':
    comp_choice = 1
  elif board[3] == board[4] == user_icon and board[5] == ' ':
    comp_choice = 5
  elif board[4] == board[5] == user_icon and board[3] == ' ':
    comp_choice = 3
  elif board[3] == board[5] == user_icon and board[4] == ' ':
    comp_choice = 4
  elif board[6] == board[7] == user_icon and board[8] == ' ':
    comp_choice = 8
  elif board[7] == board[8] == user_icon and board[6] == ' ':
    comp_choice = 6
  elif board[6] == board[8] == user_icon and board[7] == ' ':
    comp_choice = 7

  # Vertical Check
  elif board[0] == board[3] == user_icon and board[6] == ' ':
    comp_choice = 6
  elif board[3] == board[6] == user_icon and board[0] == ' ':
    comp_choice = 0
  elif board[0] == board[6] == user_icon and board[3] == ' ':
    comp_choice = 3
  elif board[1] == board[7] == user_icon and board[4] == ' ':
    comp_choice = 4
  elif board[1] == board[4] == user_icon and board[7] == ' ':
    comp_choice = 7
  elif board[4] == board[7] == user_icon and board[1] == ' ':
    comp_choice = 1
  elif board[2] == board[5] == user_icon and board[8] == ' ':
    comp_choice = 8
  elif board[5] == board[8] == user_icon and board[2] == ' ':
    comp_choice = 2
  elif board[2] == board[8] == user_icon and board[5] == ' ':
    comp_choice = 5
  # diagonal check
  elif board[0] == board[4] == user_icon and board[8] == ' ':
    comp_choice = 8
  elif board[4] == board[8] == user_icon and board[0] == ' ':
    comp_choice = 0
  elif board[0] == board[8] == user_icon and board[4] == ' ':
    comp_choice = 4
  elif board[2] == board[4] == user_icon and board[6] == ' ':
    comp_choice = 6
  elif board[4] == board[6] == user_icon and board[2] == ' ':
    comp_choice = 2
  elif board[2] == board[6] == user_icon and board[4] == ' ':
    comp_choice= 4
  else:
    comp_choice = random.choice(remaining_positions)
  return comp_choice

# game function
def play_game(player):
  game = 1
  while game:
    if player == 'User':
      print(f"It is {player}'s turn.")
      user_choice = int(input("Please select a position between 1-9: "))-1

      # Validation
      while user_choice not in range(0,9) or user_choice not in remaining_positions:
        # Only allow user to select from position 1 to 9
        if user_choice not in range(0, 9):
          print("Invalid position selected.")
        # only allow user to select from the remaining positions
        elif user_choice not in remaining_positions:
          print("The position has been occupied. Please select a different position.")
        user_choice = int(input("Please select a position between 1-9: "))-1
      print(f"You selected position {user_choice + 1}.")
      board[user_choice] = user_icon
      game = check_winner(board,player)
      remaining_positions.remove(user_choice)
      display_board(board)

      player = 'Computer'
    else:
      print(f"It is {player}'s turn.")
      comp_choice = super_computer(board=board, user_icon=user_icon)
      print(f"Computer selected position {comp_choice + 1}.")
      board[comp_choice] = comp_icon
      game = check_winner(board,player)
      remaining_positions.remove(comp_choice)
      display_board(board)

      player = 'User'
  # play the game again
  play_again()

# ask the user if they want a rematch.
def play_again():
  rematch = input("Do you want to play again? Please select '1' to play and '0' to close the game: ")  
  if rematch == '1':
    # reset the board, remaining positions and user&computer's icon
    global board
    global remaining_positions
    global user_icon, comp_icon
    global player
    board = [" "] * 9
    remaining_positions = [0,1,2,3,4,5,6,7,8]
    user_icon, comp_icon = select_icon()
    player = ''

    # display the board on the screen
    display_board(board)

   #Randomly pick the first player
    player = select_turn()

    # Begin the game
    play_game(player)
  
  elif rematch == '0':
    print("Thank you for playing Tic Tac Toe.")
  else:
    print("Please select '1' to play and '0' to close the game.")
    while rematch not in ['0', '1']:
      rematch = input("Do you want to play again? Please select '1' to play and '0' to close the game: ")
 
#-----------------------------------------------
# Ask the user to select an icon
user_icon, comp_icon = select_icon()
board = [" "] * 9
remaining_positions = [0,1,2,3,4,5,6,7,8]

# display the board on the screen
display_board(board)

#Randomly pick the first player
player = select_turn()

# Begin the game
play_game(player)