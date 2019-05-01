#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  1 14:32:31 2019

@author: fubao
"""


from collections import defaultdict

# read the 

class GRIDMDP:
    
    def __init__(self):
        self.rewardDict = defaultdict(float)          # state's reward
        self.transFuncDict = defaultdict(float)       # transition model
        self.readFile()
        
    def reward(self, state):
        return self.rewardDict[state]
    
    def transFunc(oldstate, action, newstate):
        #x = 1
        return self.transFuncDict[oldstate+ '-' + action + '-' + newstate]
        
    
    def readFile(self):
        fileName = input("Enter your file name: ")
        
        print ("fileName: ", fileName)        
        

if __name__ == '__main__' :
    
    GRIDMDPObj = GRIDMDP()
