# life.py - Game of Life lab
# Name: Christopher Buchanan
# Pledge: I pledge my honor that I have abided by the Stevens Honor System

import random
import sys

def printBoard(A):
    """ this function prints the 2d list-of-lists
    A without spaces (using sys.stdout.write)."""
    for row in A:
        for col in row:
            sys.stdout.write(str(col))
        sys.stdout.write('\n')

def createOneRow(width):
    """Returns one row of zeros of width "width"...  
       You should use this in your createBoard(width, height) function."""
    row = []
    for col in range(width):
        row += [0]
    return row

def createBoard(width, height):
    """returns a 2d array with "height" rows and "width" cols."""
    A = []
    for row in range(height):
        A += [createOneRow(width)]
    return A
'''
A = createBoard(5,3)
print(createBoard(5, 3)) #[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
printBoard(A)
'''
def diagonalize(width,height):
    """creates an empty board and then modifies it
    so that it has a diagonal strip of "on" cells."""
    A = createBoard(width, height)
    for row in range(height):
        for col in range(width):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0
    return A
'''  
A = diagonalize(7,6)
print(diagonalize(7,6))
printBoard(A)
print()
'''
def innerCells(w,h):
    """returns a 2d array of all live cells (1) except for a 
    border of empty cells (0) around the edge of the 2d array."""
    A = createBoard(w, h)
    for row in range(1, h-1):
        for col in range(1, w-1):
            A[row][col] = 1
    return A
'''
A = innerCells(5,5)
printBoard(A)
print()
'''
def randomCells(w,h):
    """returns an array of randomly-assigned 1's and 0's except for the
    border of empty cells (0) as shown in the function innerCells."""
    A = createBoard(w, h)
    for row in range(1, h-1):
        for col in range(1, w-1):
            A[row][col] = random.choice([0,1])
    return A
'''
A = randomCells(5,5)
printBoard(A)
print()
'''
def copy(A):
    """creates a new set of cells through the method of deep copying
    without regard to an old "generation" that it might depend on."""
    copy = []
    height = len(A)
    width = len(A[0])
    for row in range(height):
        newRow = []
        for col in range(width):
            newRow.append(A[row][col])
        copy.append(newRow)
    return copy
'''
oldA = createBoard(2,2)
printBoard(oldA)
print()
newA = copy(oldA)
printBoard(newA)
print()
oldA[0][0]=1
printBoard(oldA)
print()
printBoard(newA)
'''
def innerReverse(A):
    """creates a new set of cells through the function copy(A); 
    switches all 0's to 1's and all 1's to 0's."""
    oldA = copy(A)
    height = len(oldA)
    width = len(oldA[0])
    for row in range(1,height-1):
        for col in range(1,width-1):
            if oldA[row][col] == 1:
                oldA[row][col] = 0
            else:
                oldA[row][col] = 1
    return oldA
'''
A = randomCells(8,8)
printBoard(A)
print()
A2 = innerReverse(A)
printBoard(A2)
'''
def countNeighbors(row,col,A):
    """returns the number of live neighbors for a 
    cell in the board A at a particular row and col."""
    count = 0
    for r in range(row-1, row+2):
        for c in range(col-1, col+2):
            if (not(r == row) and A[r][c] == 1) or (not(c == col) and A[r][c] == 1):
                count+=1
            #if (r != row or c != col) and A[r][c] == 1:
                #count+=1
    return count

def next_life_generation(A):
    """makes a copy of A and then advanced one generation
    of Conway's game of life within the *inner cells* of 
    that copy. The outer edge always stays 0."""
    newA = copy(A)
    height = len(newA)
    width = len(newA[0])
    for row in range(height):
        for col in range(width):
            if row == 0 or col == 0 or row == height-1 or col == width-1:
                newA[row][col] = 0
            else:
                if countNeighbors(row,col,A) < 2:
                    newA[row][col] = 0
                if countNeighbors(row,col,A) > 3:
                    newA[row][col] = 0
                if countNeighbors(row,col,A) == 3 and A[row][col] == 0:
                    newA[row][col] = 1
    return newA

A = [ 
 [0,0,0,0,0],
 [0,0,1,0,0],
 [0,0,1,0,0],
 [0,0,1,0,0],
 [0,0,0,0,0]
 ]
printBoard(A)
print()
A2 = next_life_generation(A)
printBoard(A2)
print()
A3 = next_life_generation(A2)
printBoard(A3)

print()
print()

A = [ 
 [0,0,0,0,0],
 [0,0,1,0,0],
 [0,0,0,1,0],
 [0,0,0,0,1],
 [0,0,0,0,0]
 ]
printBoard(A)
print()
A2 = next_life_generation(A)
printBoard(A2)
print()
A3 = next_life_generation(A2)
printBoard(A3)
