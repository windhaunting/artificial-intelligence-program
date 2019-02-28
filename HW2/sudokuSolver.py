#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 12:25:42 2019

@author: fubao
"""

import csv

#sudoku solver using plain backtracking
rMaxLen = cMaxLen = 9         # row and col max length

def readSudokuFile(fileInput):
    # read the sudoku file into a two dimensional matrix
    ln = 0
    sudoMat = [[0 for i in range(0, rMaxLen)] for j in range(0, cMaxLen)]
    
    with open(fileInput, 'r') as f:
        for line in f:
            rV = line.rstrip().split(" ")     # row's value list
            print ("rV: ", type(rV), rV)

            for i, v in enumerate(rV):
                if v == '-':
                    continue
                sudoMat[ln][i] = int(v)
            ln += 1
    print ("sudoMat: ", sudoMat)
        
    return sudoMat
    
    
def writeSudokuFile(sudoMat, fileOut):
    with open(fileOut, 'w') as f:
        writer = csv.writer(f, delimiter=' ')
        writer.writerows(sudoMat)
   
def checkRowConflict(sudoMat, row, val):
    # check the val is used in this row already or not
    for j in range(0, cMaxLen):
        if sudoMat[row][j] == val:
            return True
    return False

def checkColumnConflict(sudoMat, col, val):
    # check the val is used in this row already or not
    for i in range(0, rMaxLen):
        if sudoMat[i][col] == val:
            return True
    return False

def checkSubGridConflict(sudoMat, row, col, val):
    for i in range(0, rMaxLen//3):
        for j in range(0, cMaxLen//3):
            if sudoMat[i+row-row%3][j+col-col%3] == val:
                return True
    return False

    
def findEmptyPosition(sudoMat):
    for i in range(0, rMaxLen):
        for j in range(0, cMaxLen):
            if sudoMat[i][j] == 0:
                return (i, j)
    return None

def checkPosNoConflictsMatrix(sudoMat,row,col,val): 
    # check a (row, col) is safe
    
    return not checkRowConflict(sudoMat, row, val)  \
      and not checkColumnConflict(sudoMat, col, val)  \
      and not checkSubGridConflict(sudoMat, row, col, val)
      
def sudoSolverBacktracking(sudoMat):
    # not finding empty row
    pos = findEmptyPosition(sudoMat) 
    if pos == None:     
        return True
   
    row = pos[0]
    col = pos[1]
    for val in range(1, 10):
        if  checkPosNoConflictsMatrix(sudoMat,row,col,val):
            sudoMat[row][col] = val       # attempt to assign a value
            print ("row, col: ", row, col, val)

            if sudoSolverBacktracking(sudoMat):   #  recursive
                return True
            
            #failure, recover it
            sudoMat[row][col] = 0
            
    return False
    
        
if __name__ == '__main__':
    fileInput = "puzzles/puz-001.txt"
    sudoMat = readSudokuFile(fileInput)
    sudoSolverBacktracking(sudoMat)
    
    print ("solved sudoMat: ", sudoMat)
    
    fileOut = fileInput.split(".")[0] + "_out.txt"
    writeSudokuFile(sudoMat, fileOut)