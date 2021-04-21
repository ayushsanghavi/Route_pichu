#!/usr/local/bin/python3
#
# route_pichu.py : a maze solver
#
# Submitted by : Ayush Sanghavi || IU username:sanghavi
#
# Based on skeleton code provided in CSCI B551, Spring 2021.
import sys
import json

# Parse the map from a given filename
def parse_map(filename):
        with open(filename, "r") as f:  # added filename in read mode
                return [[char for char in line] for line in f.read().rstrip("\n").split("\n")]  # returning contents of file as characters


# Return a string with the board rendered in a human/pichu-readable format
def printable_board(board):
        return "\n".join([" ".join(row) for row in board]) # revamping the content of file in the format we want

                
# Check if a row,col index pair is on the map
def valid_index(pos, n, m):
        return 0 <= pos[0] < n and 0 <= pos[1] < m # Here, we are checking if the position of any cell in the matrix is valid or not.
                                                   # The row index should not exceed the number of rows and the column index should not exceed the number of columns.


# Find the possible moves from position (row, col)
def moves(map, row, col):
        moves = ((row+1, col), (row-1, col), (row, col-1), (row, col+1)) # The possible moves from a particular position can only be plus one upwards/downwards/rightwards/leftwards.

# Return only moves that are within the board and legal (i.e. go through open space ".")
        return [move for move in moves if valid_index(move, len(map), len(map[0])) and (map[move[0]][move[1]] in ".@")]

# The IDEA of the below code was taken from https://codereview.stackexchange.com/questions/125286/moving-around-in-a-2d-grid
def directions(curr_move,move,path):
        if curr_move[0] - move [0] == 1:
                path = path + "U"
        elif curr_move[0] - move [0] == -1:
                path = path + "D"
        elif curr_move[1] - move[1] == 1:
                path = path + "L"
        elif curr_move[1] - move[1] == -1:
                path = path + "R"
        # print(path)
        return path

# Perform search on the map
#
# This function MUST take a single parameter as input -- the house map --
# and return a tuple of the form (move_count, move_string), where:
# - move_count is the number of moves required to navigate from start to finish, or -1
#    if no such route exists
# - move_string is a string indicating the path, consisting of U, L, R, and D characters
#    (for up, left, right, and down)
#
def search(house_map):
        # Find pichu start position
        pichu_loc = [(row_i, col_i) for col_i in range(len(house_map[0])) for row_i in range(len(house_map)) if house_map[row_i][col_i] == "p"][0]
        fringe = [(pichu_loc, 0,"")]
        visited = []
        move_string = ''

        while fringe:
                (curr_move, curr_dist,curr_path) = fringe.pop()
                move_string = curr_path
                visited.append(curr_move)
                # print (visited)

                for move in moves(house_map, *curr_move):
                        if house_map[move[0]][move[1]] == "@":
                                return (curr_dist+1, directions(curr_move,move,move_string))
                        elif move not in visited:
                                fringe.append((move, curr_dist + 1,directions(curr_move,move,move_string)))




# Main Function
if __name__ == "__main__":
        house_map = parse_map(sys.argv[1])
        print("Routing in this board:\n" + printable_board(house_map) + "\n")
        print("Shhhh... quiet while I navigate!")
        # print("helloworld")

        solution = search(house_map)
        # print("working!)
        if solution == None:
                a = -1
                print("Path=" ,a)

        else:
                print("Here's the solution I found:")
                print(str(solution[0]) + " " + str(solution[1]))



# Updated - Final.
