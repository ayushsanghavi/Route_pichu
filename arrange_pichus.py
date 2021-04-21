#!/usr/local/bin/python3
#
# arrange_pichus.py : arrange agents on a grid, avoiding conflicts
#
# Submitted by : Ayush Sanghavi | IU username: sanghavi
#
# Based on skeleton code in CSCI B551, Spring 2021
#
import sys

# Parse the map from a given filename
def parse_map(filename):
	with open(filename, "r") as f:
		return [[char for char in line] for line in f.read().rstrip("\n").split("\n")]

# Count total # of pichus on board
def count_pichus(board):
    return sum([ row.count('p') for row in board ] )

# Return a string with the board rendered in a human-pichuly format
def printable_board(board):
    return "\n".join(["".join(row) for row in board])

# Add a pichu to the board at the given position, and return a new board (doesn't change original)
def add_pichu(board, row, col):
    # print("hello") - for debugging purposes
    flag = True # a flag that will take boolean values as and when required

    # Looping from left to right through each row of the map
    for i in range (col+1, len(board[0])):
      if board[row][i] == "p":
         flag = False
         break
      elif board[row][i] == "X":
          break

    # Looping from right to left through each row of the map
    for i in range(col-1, 0, -1):
      if board[row][i] == "p":
        flag = False
        break
      elif board[row][i] == "X":
        break

    # Looping from up to down through each column of the map
    for j in range(row+1, len(board)):
      if board[j][col] == "p":
        flag = False
        break
      elif board[j][col] == "X":
        break

    # Looping from down to up through each column of the map
    for j in range(row-1, 0, -1):
      if board[j][col] == "p":
        flag = False
        break
      elif board[j][col] == "X":
        break

    if flag is True: # if the flag is true, i.e if all conditions are satisfied correctly, we add a "p" and return the new board
     return board[0:row] + [board[row][0:col] + ['p',] + board[row][col+1:]] + board[row+1:]
    else:
     return []

# Get list of successors of given board state
def successors(board):
    return [ add_pichu(board, r, c) for r in range(0, len(board)) for c in range(0,len(board[0])) if board[r][c] == '.' ]

# check if board is a goal state
def is_goal(board, k):
    return count_pichus(board) == k 


# Arrange agents on the map
#
# This function MUST take two parameters as input -- the house map and the value k --
# and return a tuple of the form (new_map, success), where:
# - new_map is a new version of the map with k agents,
# - success is True if a solution was found, and False otherwise.
#
def solve(initial_board, k):
    fringe = [initial_board]
    while len(fringe) > 0:
        for s in successors (fringe.pop()):
            if is_goal(s, k):
                return(s,True)
            fringe.append(s)
    return ([],False)

# Main Function
if __name__ == "__main__":
    house_map = parse_map(sys.argv[1])

    # This is K, the number of agents
    k = int(sys.argv[2])
    print ("Starting from initial board:\n" + printable_board(house_map) + "\n\nLooking for solution...\n")
    (newboard, success) = solve(house_map, k)
    print ("Here's what we found:")
    print (printable_board(newboard) if success else "None")

# Updated - Final.