# File: proj2.py
# Author: Uzoma Uwanamodo
# Date: 11/30/2016
# Section: 05
# E-mail: uu3@umbc.edu
# Description:
# A Program that finds paths through mazes
# Collaboration:
# Collaboration was not allowed on this assignment


################## DEBUGGING #########################


import sys
import logging
logging.basicConfig(level=logging.DEBUG, format='\n%(asctime)s - %(levelname)s :\n%(message)s\n')
import traceback
import inspect


def getParentheticalText(text,i=-1,j=0):
    
    
    if "," in text:
        if "(" in text:
            k,l = text.index("("),text.index(",")
            if l<k:
                print(k,l)
                return [text[:l]]+getParentheticalText(text[l+1:])
        else:
            return text.split(",")
    
    if not text:
        return []
    
    
    if "(" not in text[i+1:]:
#        if not text[j:]:
        if ")" not in text[i+1:]:
                return [text]
        return [text[:j+1]]+getParentheticalText(text[j+1:])
#        else
    k,l = text.index("(",i+1),text.index(")",j+1)
    
    if "(" not in text[i+1:] or (k >= j and j):
            return text[:j+1]
    
    
    
    return getParentheticalText(text,k,l)


def func(*var):
#    print(inspect.stack()[-2][4])
    code = ([i[3] for i in traceback.extract_stack()])
    code = list(filter(lambda x:"debug" in x,code))[0]
#    print(code)
    start = 13 if "vars()," in code else 6
    varNames = getParentheticalText(code[start:-1])
#    varNames = getParentheticalText()
    return ["%s: %s" % (varNames[i],var[i]) for i in range(len(var))]
    

 # debug
def debug(args,*var):
    if not "vars()" in ",".join([i for i in [i[3] for i in traceback.extract_stack()][:-1]]):
        var = list(var)
        var = [args] + var
        args=func(*var)
    elif var:
        args = ["%s: %s" % (i,args[i]) for i in args]
        args += var
#    print(args)
    return logging.debug("\n".join(["%s"] * len(args)),*args)

################## DEBUGGING #########################


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
    directionsToCheck = (list(filter(lambda z:z!=prevDirection,range(4))) + ([prevDirection] if prevDirection > -1 else []))
    for x in directionsToCheck:
        if not current[x]:
            debug(currentCoordinates,endPoint,x,current,prevDirection,directionsToCheck)   
            return [str(currentCoordinates)] +  searchMaze(maze, [(i,j+1),(i+1,j),(i,j-1),(i-1,j)][x],((x + 2) % 4),endPoint)
            
    print("No solution found")
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