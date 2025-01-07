# Description: This file contains the functions to solve a sudoku board using backtracking algorithm.
# The solve function takes a 9x9 sudoku board as input and returns the solved board.
# The check function checks if a number can be placed in a cell of the board.
def check(row,col,board,num):
    #Checks entire row
    for x in range(9):
        if board[row][x] == num:
            return False
    
    #Checks entire column
    for y in range(9):
        if board[y][col] == num:
            return False
        
    #Checks 3x3 grid
    i=(row//3)*3
    j=(col//3)*3
    for m in range(3):
        for n in range(3):
            if board[i+m][j+n] == num:
                return False
            
    return True

#Function to fully solve the board
def solve(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for num in range(1,10):
                    if check(i,j,board,num):
                        board[i][j] = num
                        if solve(board):
                            return board
                        board[i][j] = 0
                return False
    return board


