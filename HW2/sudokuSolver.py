#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 12:25:42 2019

@author: fubao
"""

import csv
import os
import glob

from common import Sudoku


#sudoku solver using plain backtracking
rMaxLen = cMaxLen = 9         # row and col max length
guesses = 0


def readSudokuFile(fileInput):
    # read the sudoku file into a two dimensional matrix
    ln = 0
    sudoMat = [[0 for i in range(0, rMaxLen)] for j in range(0, cMaxLen)]
    
    with open(fileInput, 'r') as f:
        for line in f:
            rV = line.rstrip().split(" ")     # row's value list
            #print ("rV: ", type(rV), rV)

            for i, v in enumerate(rV):
                if v == '-':
                    continue
                sudoMat[ln][i] = int(v)
            ln += 1
    #print ("sudoMat: ", sudoMat)
        
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

def checkPosAllNoConflictsMatrix(sudoMat,row,col,val): 
    # check a (row, col) is safe globally
    
    return not checkRowConflict(sudoMat, row, val)  \
      and not checkColumnConflict(sudoMat, col, val)  \
      and not checkSubGridConflict(sudoMat, row, col, val)
      
def sudoSolverBacktracking(sudoMat):
    
    # not finding empty row
    pos = findEmptyPosition(sudoMat) 
    if pos == None:     
        return True
   
    global guesses 

    row = pos[0]
    col = pos[1]
    for val in range(1, 10):
        guesses += 1
        #print ("guess: ", guesses)
        if  checkPosAllNoConflictsMatrix(sudoMat,row,col,val):
            sudoMat[row][col] = val       # attempt to assign a value
            #print ("row, col: ", row, col, val)
            if sudoSolverBacktracking(sudoMat):   #  recursive
                return True
            
            #failure, recover it
            sudoMat[row][col] = 0
            
    return False
    

def getLegValOneCell(sudoMat, row, col):
    
    allDigits = range(1, 10)
    
        
    colExistVal = []
    for i in range(0, rMaxLen):
        colExistVal.append(sudoMat[i][col])
    #get subGrid initial starting coordinate for this (row, col)
    initRow = row - row%3
    inttCol = col - col%3
    
    subGridExistingValLst = []
    for i in range(0, 3):
        for j in range(0, 3):
            subGridExistingValLst.append(sudoMat[initRow+i][inttCol+j])
            
    allExistingValList = sudoMat[row] + colExistVal + subGridExistingValLst
    #get subgrid's legal values
    legalVal  = [v for v in allDigits if v not in allExistingValList]
                    
    #print (" legalVal: ", row, col, legalVal)
    
    return legalVal

def findEmptyPosLegalVal(sudoMat):
    # find all the empty position and legal values considering constraints
    emptyCellLst = []   # 
    for r in range(0, rMaxLen):
        for c in range(0, cMaxLen):
            if sudoMat[r][c] == 0:
                cell = (r, c)
                legalVal = getLegValOneCell(sudoMat, r, c)
                emptyCellLst.append((cell, legalVal))
            
    return sorted(emptyCellLst)


def sudoSolverMRVBacktracking(sudoMat):
    # with MRV heuristic 
    
    # not finding empty row
    pos = findEmptyPosition(sudoMat) 
    if pos == None:     
        return True
   
    global guesses 


    
    emptyCellLst = findEmptyPosLegalVal(sudoMat)    # MRV
     
    legalValLst = emptyCellLst[0][1]
    row = emptyCellLst[0][0][0]
    col = emptyCellLst[0][0][1]
    
    for val in legalValLst:
        guesses += 1
        #print ("guess: ", guesses)
        sudoMat[row][col] = val       # attempt to assign a value
            #print ("row, col: ", row, col, val)
        if sudoSolverMRVBacktracking(sudoMat):   #  recursive
            return True
            
        #failure, recover it
        sudoMat[row][col] = 0
            
    return False




def AC3(sudoku):

    que = list(sudoku.constraints)

    while que:

        xi, xj = que.pop(0)
        
        if revise(sudoku, xi, xj):

            global guesses
            guesses += 1
            if len(sudoku.domains[xi]) == 0:
                return False
            
            for xk in sudoku.neighbors[xi]:
                if xk != xi:
                    que.append([xk, xi])

    return True


def revise(sudoku, xi, xj):

    revised = False

    for x in sudoku.domains[xi]:
        if not any([sudoku.constraint(x, y) for y in sudoku.domains[xj]]):
            sudoku.domains[xi].remove(x)
            revised = True

    return revised


def executeAC3(sudoMat):
    # execute AC-3
    sudoku = Sudoku(sudoMat)

    if AC3(sudoku):

        if sudoku.solved():

            #write into sudoMat
            for var in sudoku.variables:
                sudoMat[int(var[0])][int(var[1])] = sudoku.domains[var][0]


            
def executeSudoSolver(method):
    # output file is in the  output folder
       
    fileInputDir = "puzzles"
    for filename in sorted(glob.glob(os.path.join(fileInputDir, '*.txt'))):
        print ("filename: ", filename)
        
        sudoMat = readSudokuFile(filename)
         
        if method == "plainBT":
            sudoSolverBacktracking(sudoMat)
        elif method == "MRVBT":
            sudoSolverMRVBacktracking(sudoMat)
        elif method == "AC-3":
            executeAC3(sudoMat)
            
        global guesses
        print ("solved sudoMat: ", sudoMat, guesses)

        outputDir = "output_" + method
        if not os.path.exists(outputDir):
            os.makedirs(outputDir)
                    
        fileOut = outputDir + "/" + filename.split("/")[1].split(".")[0] + "_out.txt"
        
        writeSudokuFile(sudoMat, fileOut) 

        guesses = 0

if __name__ == '__main__':
    print ("begin to execute plain backtracking")

    method = "plainBT"          # plain backtracking    
    executeSudoSolver(method)

    print ("begin to execute backtracking with MRV")
    method = "MRVBT"          # backtracking with MRV
    executeSudoSolver(method)
    
    print ("begin to execute AC-3 ")
    method = "AC-3"
    executeSudoSolver(method)

