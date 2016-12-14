# File: proj2.py
# Author: Uzoma Uwanamodo
# Date: 11/30/2016
# Section: 05
# E-mail: uu3@umbc.edu
# Description:
# A Program that finds paths through mazes
# Collaboration:
# Collaboration was not allowed on this assignment


import sys


WALL = 1
OPEN = 0
RIGHT,BOTTOM,LEFT,TOP = range(4)


# readMaze() take a file and parses it
# Input: filename, the name of the file
# Output: maze, the maze
def readMaze(filename):
    
    # read in file data
    mazeData = open(filename)
    
    # parse file data
    parsedMaze = [i.split() for i in list(mazeData)]
    
    # Close the file
    mazeData.close()
    
    ### Process maze data
    # Get dimension of maze
    mazeDims = tuple(parsedMaze[0])
    
    # Get coordinates of the finish
    finishCoordinates = tuple(parsedMaze[1])
    
    # Parse the maze data into a 3D Array
    maze = [parsedMaze[i:i+int(mazeDims[1])] for i in range(2,len(parsedMaze),int(mazeDims[1]))]
    
    # Add finish coordinates to maze data
    maze.append(finishCoordinates)
    
    return maze
    
    
    
# searchMaze() recursive function that search to find a way out of the maze
# Input: maze: the maze, currentCoordinates: the coordinates of the pathfinder, the number indicating the previous direction, endPoint: the coordinates of the endpoint
def searchMaze(maze,currentCoordinates,prevDirection,endPoint):
    
    ## Get current square
    # Set coordinate variables
    i,j=currentCoordinates
    
    # Retrieve square from maze
    current = list(map(lambda k:int(k),maze[i][j]))
#    debug(vars())
    
    
    if 0 not in current:
        print("No solution found")
        return
    
    if currentCoordinates == endPoint:
        print("Solution Found")
#        return 
        return [str(currentCoordinates)]
    
    # Get the direction to check, using the previous direction as the last one to check for backtracking
    directionsToCheck = (list(filter(lambda z:z!=prevDirection,range(4))))
    
    for x in directionsToCheck:
        if not current[x]:
            hello = [str(currentCoordinates)] + searchMaze(maze, [(i,j+1),(i+1,j),(i,j-1),(i-1,j)][x],((x + 2) % 4),endPoint)
            return(hello)
#    return searchMaze(maze, (i,j),((x + 2) % 4),endPoint)
    return []
    
def main():
    
    ## Welcome User
    print("Welcome to the Maze Solver!")
    
    ## Initialize Maze
    
    # Ask user for filename (or use command line file name)
    filename = (sys.argv[1:] or [input("Please enter the filename of the maze: ")])
    
    # load and parse the maze
    maze = readMaze(filename[0])
    
    
    
    ## Get Iniital Condition
    
    # Get starting row (validatad input)
    startingRow = int(input("Please enter the starting row: "))
    while not startingRow in range(len(maze)-1):
        startingRow = int(input("Invalid, enter a number between 0 and %s (inclusive): " % (len(maze)-1)))
        
    # Get starting column (validated input)
    startingColumn = int(input("Please enter the starting column: "))
    while not startingColumn in range(len(maze[0])):
        startingColumn = int(input("Invalid enter a number between 0 and %s (inclusive): " % (len(maze[0]))))
        
    ## Begin pathfinding
    print("\n".join(searchMaze(maze,(startingRow,startingColumn),-1, tuple(map(lambda x:int(x),maze[-1])))))
#    print(searchMaze(maze,(0,1),-1, tuple(map(lambda x:int(x),maze[-1]))))
main()