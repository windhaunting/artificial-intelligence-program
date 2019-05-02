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
        self.stateNum = 0
        self.actions = ['left', 'right', 'up', 'down']
        self.rewardDict = defaultdict(float)          # state's reward
        self.transFuncDict = defaultdict(list)       # transition model
        self.readFile()
        
    def reward(self, state):
        return self.rewardDict[state]
    
    def transFunc(self, oldstate, action):
        #x = 1
        return self.transFuncDict[oldstate+ '-' + action]
        
    
    def readFile(self):
        #fileName = input("Enter your file name: ")            # in current directory for convenience
        fileName = "gw2.txt"   # "simple.txt"   # "gw2.txt"    #
        print ("fileName: ", fileName)  
        
        cnt = 1
        with open(fileName) as fd:
            for line in fd:
                line = line.strip().split("\t")[0]
                print ("line: ", line)
                if cnt == 1:
                    self.stateNum = int(line)
                    #cnt += 1
                elif (cnt <= 1+self.stateNum):
                    ind = cnt - 1
                    self.rewardDict['s' + str(ind)] = float(line)
                    
                    #cnt += 1
                elif (cnt <= 1+2*self.stateNum):            # action left
                    ind = cnt - self.stateNum-1
                    key = 's' + str(ind) +'-' + 'left' 
                    
                    probs = line.strip().split(',') 
                    probStateLst = [(float(p), 's' + str(i+1)) for i, p in enumerate(probs)]
                    #for i, pr in enumerate(probs):
                    #    key = oldState +'-' + 's' + str(i+1)
                    #    self.transFuncDict[key] = pr
                    self.transFuncDict[key] = probStateLst
                    
                elif (cnt <= 1+3*self.stateNum):            # action up
                    ind = cnt - 2*self.stateNum-1
                    key = 's' + str(ind) +'-' + 'up' 
                    
                    probs = line.strip().split(',') 
                    probStateLst = [(float(p), 's' + str(i+1)) for i, p in enumerate(probs)]
                    #for i, pr in enumerate(probs):
                    #    key = oldState +'-' + 's' + str(i+1)
                    #    self.transFuncDict[key] = pr
                    self.transFuncDict[key] = probStateLst

                elif (cnt <= 1+4*self.stateNum):            # action right
                    ind = cnt - 3*self.stateNum-1
                    key = 's' + str(ind) +'-' + 'right' 
                    
                    probs = line.strip().split(',') 
                    probStateLst = [(float(p), 's' + str(i+1)) for i, p in enumerate(probs)]
                    #for i, pr in enumerate(probs):
                    #    key = oldState +'-' + 's' + str(i+1)
                    #    self.transFuncDict[key] = pr
                    self.transFuncDict[key] = probStateLst
                    
                elif (cnt <= 1+5*self.stateNum):            # action down
                    ind = cnt - 4*self.stateNum-1
                    key = 's' + str(ind) +'-' + 'down' 
                    
                    probs = line.strip().split(',')
                    probStateLst = [(float(p), 's' + str(i+1)) for i, p in enumerate(probs)]
                    #for i, pr in enumerate(probs):
                    #    key = oldState +'-' + 's' + str(i+1)
                    #    self.transFuncDict[key] = pr                        
                    self.transFuncDict[key] = probStateLst
                
                cnt += 1
        
        print ("self.rewardDict: ", self.rewardDict, self.transFuncDict, len(self.transFuncDict))
                
    
    def valueIteration(self):
        
        UNewDict = dict([('s' + str(i), 0) for i in range(1, self.stateNum+1)])         # defaultdict(float)               # k: states, v: values
        
        epsilon = 0.1       # 0.001
        gamma = 1
        while True:
            UOldDict = UNewDict.copy()
            delta = 0
            for i in range(1, self.stateNum+1):
                s = 's' + str(i)
                UNewDict[s] = self.reward(s) + gamma * max([sum([p * UOldDict[s1] for (p, s1) in self.transFunc(s, a)])
                                            for a in self.actions])
                delta = max(delta, abs(UOldDict[s] - UNewDict[s]))
                
            #print ("UDict: ", UOldDict, UNewDict)
            if delta <= epsilon:        #  * (1 - gamma) / gamma:
                 return UOldDict


if __name__ == '__main__' :
    
    GRIDMDPObj = GRIDMDP()
    UDict = GRIDMDPObj.valueIteration()
    print ("UDict: ", UDict)