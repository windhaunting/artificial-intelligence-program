#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 22:36:54 2019

@author: fubao
"""
from queue import PriorityQueue
from math import sqrt

import time
import random

from matplotlib import pyplot as plt


def plotXY(xLst, yLst, xlabel, ylabel, saveFilePath):
    
    #xlabel = "Solution length"
    #ylabel = "Data size"
    #xlim = [0, 100]
    #ylim = [0, 100000]
    #print ("plot ", )
    #title = ""  # " Runtime vs Query graph size"
    
    plt.figure(1)
    #ax.yaxis.set_major_formatter(formatter)
    
    plt.scatter(xLst, yLst, color = 'b')
    #plt.xticks(xLst, xstrLst, fontsize = 11)
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    
    #saveFilePath = '.pdf'
    plt.savefig(saveFilePath)
    plt.show()
    

# checks whether given position is  
# inside the board 
def isInside(x, y, N): 
    if (x >= -N and x <= N and 
        y >= -N and y <= N):  
        return True

    return False


def heuristic(loc1, loc2):
    
    return min(abs(loc1[0]-loc2[0]), abs(loc1[1]-loc2[1]))
    

# A star search
def AstarSearch(knightpos, targetpos, N): 
      
    #all possible movments for the knight 
    dx = [2, 2, -2, -2, 1, 1, -1, -1] 
    dy = [1, -1, 1, -1, 2, -2, 2, -2] 
      
    frontQue = PriorityQueue()      # frontier queue
      
    # push starting position of knight 
    # with 0 distance 
    frontQue.put((0, knightpos))
      
    # make all cell unvisited  
    visited = [[False for i in range(-N, N + 1)]  
                      for j in range(-N, N + 1)] 
    
    costSoFar = {knightpos: 0}
    
    # visit starting state 
    visited[knightpos[0]][knightpos[1]] = True
    visitedCnt = 1
    # loop untill we have one element in queue  
    
    startTime = time.time()
    while not frontQue.empty():
          
        t = frontQue.get()          # get the minimum cost frontQue 
        visitedCnt += 1
        #print ("tttt: ", t)
        # if current cell is equal to target  
        # cell, return its distance  
        if(t[1][0] == targetpos[0] and 
           t[1][1]== targetpos[1]): 
            # print ("visited: ",  visitedCnt)
            elapsedTime = time.time() - startTime
            # print ("endTime: ", elapsedTime)
            return t[0], visitedCnt, elapsedTime*1000
              
        # iterate for all reachable states  
        for i in range(8): 
              
            x = t[1][0]  + dx[i]    # 
            y = t[1][1]  + dy[i] 
            
            newCost = costSoFar[t[1]] +  + 1
            if(isInside(x, y, N) and ((x,y) not in costSoFar or newCost < costSoFar[(x,y)])): 
                #visited[x][y] = True
                
                costSoFar[(x,y)] = newCost
                priority = newCost + heuristic((x,y), targetpos)
                frontQue.put((priority, (x, y))) 



    
# Driver Code     
if __name__=='__main__':  
    N = 100
    #knightpos = (0, 0)
    #targetpos = (40, 30)
    # print(AstarSearch(knightpos, targetpos, N)) 
    xLst = []
    y1Lst = []
    y2Lst = []
    for i in range(0, 1000):
        randomX = random.randint(-100, 100)
        randomY = random.randint(-100, 100)
        knightpos = (0, 0)
        targetpos = (randomX, randomY)
        solLen, nodeNum, elapTime = AstarSearch(knightpos, targetpos, N)
        xLst.append(solLen)
        y1Lst.append(nodeNum)
        y2Lst.append(elapTime)
        
    plotXY(xLst, y1Lst, "Solution length", "Number of nodes expanded", "figure1_NumberofNodeExpanded.pdf")
    
    plotXY(xLst, y2Lst, "Solution length", "Computation time (ms)", "figure2_computationTime.pdf")
