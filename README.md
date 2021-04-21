# Assignment 0

Name: Ayush Sanghavi

IU Username: sanghavi

Email ID: sanghavi@iu.edu


Report contents:
# 1) Introduction: 
   
   Hello, I am Ayush Sanghavi, a graduate Computer Science student at the Luddy School Of Informatics, Computing and Engineering.
    The following report describes my contribution to the assignment 0 given to us by Prof. Dr.David Crandall under the CSCI-B551 Elements of Artificial Intelligence course.
    
# 2) Problem Statement:

   # For Part 1
   I was given a skeleton code for python and mainly had to add and modify some code.
   A house map (2D matrix) was given with N x M cells. 
   The map had the following characters : 
   
   'p' - pichu (our agent)
   
   'X' - wall
   
   '.' - open space where agent can travel
   
   '@' - goal state
   
   If passed a map as an input argument, I was suppose to write code where the agent can fly and reach the goal state (@) using blind search technique. 
   I also have to return the correct directions, the pichu (agent) has traversed along with the number of steps taken to reach the goal state.
   
   # For Part 2

   For par 2, I was given a skeleton code for python and mainly had to add "n" pichus (agents) such that they cannot see each other.
   If the map has "X", it means there is a wall and the pichus can be placed on either side.
   We have to pass the map and the number of agents (n) as arguments. Based on the input, the agents will arrange themselves according to the given condition.
   The map had the following characters:
   'p' - pichu (our agent)
   
   'X' - wall
   
   '.' - open space where agent can travel
   
   '@' - me

   
   After the map and the number of agents passed, I wrote a code by which the pichus have to arrange themselves accordingly according to the given conditions.
   i.e They should not be visible to each other. 
   
   "." character acts as a field of visibility and "X" on the map is a wall and will cease visibility across.
   
# 3) My contribution:


   #  For Part 1

   Because, the skeleton code was given to us in advance, it was much easier for me to catch up with what is actually happening in the code.
   I went through it thoroughly, it took me about two days to actually understand what's happening and what do we have to do.
   After some examination, I realized I have to allow the pichu (agent) to traverse from the initial state to the goal state and count the number of steps taken and also print the path from initial state to the goal state.
   I created a function "directions". The idea of moving in a 2D matrix in a python was taken from https://codereview.stackexchange.com/questions/125286/moving-around-in-a-2d-grid. 
   I have mentioned the same in my code as a comment.
   I have passed curr_move (Current move), move (Move prior to current move), path (an empty string that will log my path).
   
   After creating the function, I am computing whether the agent is going up, down, left or right by finding the index difference of the current move and the previous move.
   I am returning the path string depending on where the move step has been taken.
   
   The algorithm used to search the goal state is Depth First Search.
   
   In the search function, I have created a list called visited. It will append the moves, the pichu (agent) has traversed.
   If the goal state is found, I have called the directions function by passing the necessary parameters. (Current state, state prior to the current state and an empty string that will record the correct paths taken to reach the goal state.)
   else
   
   I am appending the nodes that are not in the visited list in the fringe. (Nodes that are not in the visited list)
   
   In the main function,
   if the solution is None (If no solution is found), I am printing that the path = -1.
   else
   
   Printing the 0th and the 1st element of the tuple. 
   
   0th element of the tuple : The number of steps taken by the agent to reach from the initial state to the goal state.
   
   1st element of the tuple : The path from the initial state to the goal state.
   
   # For Part 2
   
   I saw the skeleton code that was given to us and understood it. 
   The main aim was to add the pichus according to the given conditions.
   
   I have not added any new functions here.
   
   Since we just had to add pichus correctly, I have ammended the add_pichu function itself.
   
   I have added four for loops. 
   Two loops would iterate through the rows, one would go from right to left and the other left to right.
   The other two loops would iterate through the columns, one would go from up to down and the other from down to up.
   If a "p" is found, then flag would switch to false.
   
   If an "X" is found and if all the loops don't switch the flag to false, then a "p" is added correctly
   
# 4) Problems faced:

   # For Part 1
   I am not as proficient in python as much as I am in Java. I had to spend some time outside the course to learn considerable amount of basics of Python.
   I saw the following video https://youtu.be/rfscVS0vtbw on speed 1.25x.
   It helped me clear the basics of python along with some syntax and data structures like list, dictionary and tuples. 
   I had to make sure that the optimal solution is printed along with the path and for that we had to add add U,D,L,R in the path accordingly to reach the goal state.
   It took me time to think how to traverse the 2D matrix and log the path and found a few resources on Google. I did a lot of trials and errors and finally got it right. I have already cited the resource I used for the directions function.
   The next hurdle was that, my program went to an infinite loop. (Because the pichu - our agent was continuously moving from one node to another).
   I realised that DFS can be improved by neglecting and not backtracking to the visited nodes.
   I made a list that will keep a record of the visited nodes.
   If the next move is not in visited list, it would only then take the next move.
   
   In my code, I have printed a lot of things while testing, however since, they are now redundant, I have commented those out.
   
   # For Part 2
   It took me quite some time for me to find out the correct indexing for loop iteration in all directions.
   A lot of trials and errors while running the code.
   I was running a lot of test cases.
   For larger inputs, the algorithm runs a little slow and then adds the pichus.
   If all the conditions satisfy and if the flag is true then the correct board is returned 
   
   else 
   
   an empty list is returned.
   

# 6) Answers for the questions in part 2
   
   1. State Space: Each "." node in the input map will be the possible places where "p" can be placed and hence that would be our state space.
   2. Initial State: A map with one "p"
   3. Successor Function: Correctly placing a "p" such that no other "p" can see each other at any instance not considering the diagonals.
   4. Goal State: The Map arranged with all the n "p" correctly such that no "p" can see each other. (n = input to adopt the number of "p")
   5. Cost Function: The cost required would be (number of "p" to be arranged) * (cost to place one single "p").
   
.