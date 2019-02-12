#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 00:06:31 2019

@author: fubao
"""

# Question Q-6

import sys 
import random
import time

from Q5_3_AStar_ChessKnight import plotXY

def generateTSPInstance(numberCities):    
    
    cities = []
    for i in range(numberCities):
        x = random.random()               # 0, 1
        y = random.random()
        cities.append((x,y))
    
    
    #print ("cities: ", cities)
    
'''

  
class Graph(): 
  
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
  
    def printMST(self, parent): 
        print ("Edge \tWeight")
        for i in range(1,self.V): 
            print (parent[i],"-",i,"\t",self.graph[i][ parent[i] ] )
  
 
    def minKey(self, key, mstSet): 
  
        min = sys.maxsize 
  
        for v in range(self.V): 
            if key[v] < min and mstSet[v] == False: 
                min = key[v] 
                min_index = v 
  
        return min_index 
  

    def primMST(self): 
  
        expandedCnt = 0
        #Key values used to pick minimum weight edge in cut 
        key = [sys.maxsize] * self.V 
        parent = [None] * self.V # Array to store constructed MST 

        key[0] = 0 
        mstSet = [False] * self.V 
  
        parent[0] = -1 # First node is always the root of 
  
        for cout in range(self.V): 
  
            u = self.minKey(key, mstSet) 
            
            mstSet[u] = True

            for v in range(self.V): 
               
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]: 
                        key[v] = self.graph[u][v] 
                        parent[v] = u 
                        
                        expandedCnt += 1
                        
        self.printMST(parent)
        return expandedCnt
              
                      
if __name__=='__main__':  

    numberCities = 100
    generateTSPInstance(numberCities) 
    
    g = Graph(numberCities) 
    g.graph = [[random.randint(0, 10) for i in range(numberCities)]  
                    for j in range(numberCities)] 
    
   
    startTime = time.time()
    expandedCnt = g.primMST(); 
    elapsedTime = time.time() - startTime
    print ("elapsedTime: ", elapsedTime, expandedCnt)
'''

import numpy as np
import sys


def check_unvisited_node(unvisited):
    for u in unvisited:
        if u == 1:
            return True
    return False


def get_unvisited_node(unvisited):
    for index, node in enumerate(unvisited):
        if node == 1:
            return index
    return -1


def find_best_route(node_no, travel_route, min_distance):
    shortest_travel_route = travel_route[0]
    shortest_min_distance = min_distance.item(0)
    for start_node in range(0, node_no):
        if min_distance[start_node] < shortest_min_distance:
            shortest_min_distance = min_distance.item(start_node)
            shortest_travel_route = travel_route[start_node]

    print("min distance is: " + str(shortest_min_distance))
    print("travel route is: ")
    print(shortest_travel_route)

    return shortest_min_distance, shortest_travel_route


def in_travel_route(node, travel_route):
    for t in travel_route:
        if t == node:
            return True
    return False

def AstarMST(numberCities, graph):
    # Read the first line for node number
    node_no = numberCities
    #graph = [[-1, 0, 811, 717, 0, 0, 232790, 679, 359, 628, 0, 0, 0, 574, 211, 0, 518, 0, 883, 772, 0, 264, 693, 0, 0, 0, 950, 0, 0, 495, 309, 659, 819, 0, 0, 0, 0, 485, 894, 0, 1047, 0, 0, 831, 530, 254, 229],[0, -1, 0, 354, 820, 0, 0, 3163, 0, 402, 0, 395, 78, 0, 286, 0, 662, 449, 0, 510, 383, 0, 0, 0, 790, 0, 0, 504, 0, 769, 128, 689, 453, 147, 0, 59, 499, 142, 0, 572, 0, 0, 0, 628, 0, 0, 0],[811, 0, -1, 0, 0, 792, 231158, 1670, 1227, 1501, 161, 0, 0, 1750, 0, 205, 1572, 439, 1787, 1833, 883, 0, 0, 0, 435, 0, 0, 0, 934, 1448, 1794, 0, 0, 0, 0, 843, 0, 0, 0, 0, 0, 529, 0, 0, 0, 1353, 1707],[717, 354, 0, -1, 0, 841, 0, 2197, 834, 0, 864, 0, 1031, 0, 1334, 0, 863, 0, 469, 345, 0, 0, 0, 0, 0, 0, 0, 1391, 0, 0, 418, 0, 1971, 607, 355, 0, 0, 1535, 0, 0, 0, 1007, 886, 1789, 1830, 800, 0],[0, 820, 0, 0, -1, 772, 0, 4788, 0, 548, 141, 0, 894, 289, 0, 0, 0, 0, 595, 620, 0, 0, 0, 753, 0, 444, 0, 0, 0, 0, 700, 136, 973, 673, 915, 1005, 1684, 0, 903, 1959, 419, 511, 376, 500, 0, 575, 0],[0, 0, 792, 841, 772, -1, 232048, 0, 301, 0, 1335, 0, 0, 0, 0, 1819, 472, 655, 956, 857, 174, 0, 0, 0, 0, 1671, 998, 387, 0, 0, 0, 0, 943, 0, 0, 450, 635, 0, 1006, 258, 0, 2071, 2341, 894, 0, 198, 367],[232790, 0, 231158, 0, 0, 232048, -1, 444, 0, 623, 0, 693, 827, 0, 810, 0, 0, 0, 758, 739, 0, 0, 0, 0, 159, 0, 234637, 0, 232174, 0, 636, 231013, 0, 0, 857, 0, 421, 762, 233823, 0, 232579, 0, 631, 664, 111, 0, 764],[679, 3163, 1670, 2197, 4788, 0, 444, -1, 0, 234, 321, 3943, 652, 436, 0, 263, 0, 4346, 0, 0, 3722, 0, 0, 0, 4182, 0, 0, 358, 0, 665, 0, 243, 656, 0, 2968, 0, 0, 490, 587, 0, 368, 623, 386, 222, 487, 550, 679],[359, 0, 1227, 834, 0, 301, 0, 0, -1, 0, 339, 0, 0, 0, 557, 309, 171, 487, 792, 726, 0, 0, 0, 0, 0, 640, 781, 144, 0, 0, 0, 0, 933, 453, 0, 0, 0, 0, 945, 0, 824, 0, 0, 0, 0, 0, 0],[628, 402, 1501, 0, 548, 0, 623, 234, 0, -1, 524, 0, 478, 601, 654, 0, 0, 124, 257, 0, 0, 0, 1663, 2219, 0, 193, 0, 444, 732, 780, 347, 452, 425, 304, 0, 443, 208, 286, 0, 0, 524, 741, 567, 225, 0, 0, 550],[0, 0, 161, 864, 141, 1335, 0, 321, 339, 524, -1, 594, 801, 155, 0, 0, 0, 0, 0, 0, 734, 924, 0, 0, 0, 469, 0, 0, 782, 0, 606, 0, 946, 584, 0, 729, 316, 0, 0, 386, 0, 0, 499, 536, 0, 0, 0],[0, 395, 0, 0, 0, 0, 693, 3943, 0, 0, 594, -1, 467, 0, 0, 521, 626, 0, 248, 0, 704, 817, 202, 0, 0, 0, 0, 507, 0, 842, 362, 0, 357, 0, 0, 0, 278, 0, 311, 0, 559, 804, 0, 244, 701, 643, 557],[0, 78, 0, 1031, 894, 0, 827, 652, 0, 478, 801, 467, -1, 782, 246, 0, 722, 0, 715, 580, 372, 396, 0, 441, 0, 670, 852, 565, 404, 810, 195, 761, 480, 220, 42, 75, 0, 205, 593, 614, 996, 0, 0, 703, 0, 0, 155],[574, 0, 1750, 0, 289, 0, 0, 436, 0, 601, 155, 0, 782, -1, 0, 0, 0, 0, 750, 0, 0, 0, 840, 518, 144, 0, 686, 0, 688, 262, 592, 217, 1005, 0, 813, 0, 404, 724, 0, 262, 0, 222, 0, 658, 0, 326, 0],[211, 286, 0, 1334, 0, 0, 810, 0, 557, 654, 0, 0, 246, 0, -1, 0, 702, 0, 908, 781, 0, 0, 0, 286, 778, 0, 1014, 561, 0, 0, 0, 0, 726, 0, 0, 229, 0, 0, 0, 532, 1137, 0, 1157, 877, 0, 0, 106],[0, 0, 205, 0, 0, 1819, 0, 263, 309, 0, 0, 521, 0, 0, 0, -1, 166, 0, 577, 0, 0, 865, 0, 0, 0, 415, 0, 0, 728, 0, 0, 0, 0, 508, 750, 654, 244, 625, 0, 0, 0, 0, 502, 484, 236, 396, 693],[518, 662, 1572, 863, 0, 472, 0, 0, 171, 0, 0, 626, 722, 0, 702, 166, -1, 442, 723, 687, 589, 0, 0, 465, 169, 563, 674, 157, 634, 0, 533, 0, 0, 0, 754, 647, 369, 0, 938, 0, 0, 0, 0, 0, 0, 0, 0],[0, 449, 439, 0, 0, 655, 0, 4346, 487, 124, 0, 0, 0, 0, 0, 0, 442, -1, 308, 0, 656, 806, 387, 600, 612, 176, 0, 0, 710, 0, 360, 328, 548, 0, 0, 476, 83, 0, 0, 523, 475, 0, 0, 0, 0, 512, 566],[883, 0, 1787, 469, 595, 956, 758, 0, 792, 257, 0, 248, 715, 750, 908, 577, 723, 308, -1, 0, 935, 1317, 0, 897, 891, 0, 198, 0, 989, 0, 603, 553, 0, 0, 707, 690, 359, 511, 358, 829, 0, 0, 0, 95, 800, 820, 803],[772, 510, 1833, 345, 620, 857, 739, 0, 726, 0, 0, 0, 580, 0, 781, 0, 687, 0, 0, -1, 819, 935, 259, 793, 0, 185, 0, 0, 0, 0, 0, 549, 381, 437, 571, 559, 319, 0, 0, 0, 484, 879, 542, 0, 763, 0, 0],[0, 383, 883, 0, 0, 174, 0, 3722, 0, 0, 734, 704, 372, 0, 0, 0, 589, 656, 935, 819, -1, 193, 721, 0, 640, 831, 0, 0, 0, 0, 0, 0, 837, 385, 0, 325, 0, 0, 923, 395, 1112, 0, 1122, 0, 600, 0, 0],[264, 0, 0, 0, 0, 0, 0, 0, 0, 0, 924, 817, 396, 0, 0, 865, 0, 806, 1317, 935, 193, -1, 0, 323, 830, 0, 1160, 658, 155, 736, 0, 0, 0, 501, 0, 0, 821, 583, 988, 0, 0, 0, 1291, 1026, 0, 0, 0],[693, 0, 0, 0, 0, 0, 0, 0, 0, 1663, 0, 202, 0, 840, 0, 0, 0, 387, 0, 259, 721, 0, -1, 737, 0, 426, 571, 0, 766, 979, 385, 0, 165, 0, 0, 0, 470, 0, 202, 792, 742, 0, 0, 0, 0, 749, 0],[0, 0, 0, 0, 753, 0, 0, 0, 0, 2219, 0, 0, 441, 518, 286, 0, 465, 600, 897, 793, 0, 323, 737, -1, 0, 0, 0, 359, 0, 0, 0, 0, 871, 383, 0, 0, 587, 534, 935, 264, 1033, 416, 1036, 838, 0, 193, 0],[0, 790, 435, 0, 0, 0, 159, 4182, 0, 0, 0, 0, 0, 144, 778, 0, 169, 612, 891, 0, 640, 830, 0, 0, -1, 730, 0, 301, 675, 0, 0, 361, 0, 0, 877, 0, 0, 0, 0, 246, 826, 0, 0, 0, 0, 321, 0],[0, 0, 0, 0, 444, 1671, 0, 0, 640, 193, 469, 0, 670, 0, 0, 415, 563, 176, 0, 185, 831, 0, 426, 0, 730, -1, 0, 0, 886, 0, 523, 391, 0, 0, 671, 629, 206, 0, 467, 681, 331, 772, 0, 0, 0, 0, 0],[950, 0, 0, 0, 0, 998, 234637, 0, 781, 0, 0, 0, 852, 686, 1014, 0, 674, 0, 198, 0, 0, 1160, 571, 0, 0, 0, -1, 640, 1065, 933, 707, 0, 685, 0, 851, 0, 0, 0, 556, 825, 175, 891, 241, 0, 0, 833, 914],[0, 504, 0, 1391, 0, 387, 0, 358, 144, 444, 0, 507, 565, 0, 561, 0, 157, 0, 0, 0, 0, 658, 0, 359, 301, 0, 640, -1, 0, 0, 0, 0, 816, 367, 0, 0, 0, 516, 0, 185, 695, 297, 688, 566, 0, 198, 506],[0, 0, 934, 0, 0, 0, 232174, 0, 0, 732, 782, 0, 404, 688, 0, 728, 634, 710, 989, 0, 0, 155, 766, 0, 675, 886, 1065, 0, -1, 581, 395, 0, 0, 0, 0, 0, 713, 555, 0, 0, 1167, 579, 1176, 0, 0, 0, 0],[495, 769, 1448, 0, 0, 0, 0, 665, 0, 780, 0, 842, 810, 262, 0, 0, 0, 0, 0, 0, 0, 736, 979, 0, 0, 0, 933, 0, 581, -1, 0, 474, 1138, 657, 0, 735, 612, 0, 0, 196, 946, 0, 917, 885, 193, 0, 0],[309, 128, 1794, 418, 700, 0, 636, 0, 0, 347, 606, 362, 195, 592, 0, 0, 533, 360, 603, 0, 0, 0, 385, 0, 0, 523, 707, 0, 395, 0, -1, 0, 521, 0, 0, 126, 0, 183, 0, 0, 836, 0, 0, 0, 585, 393, 206],[659, 689, 0, 0, 136, 0, 231013, 243, 0, 452, 0, 0, 761, 217, 0, 0, 0, 328, 553, 549, 0, 0, 0, 0, 361, 391, 0, 0, 0, 474, 0, -1, 877, 541, 0, 692, 244, 649, 0, 0, 472, 433, 448, 458, 0, 452, 0],[819, 453, 0, 1971, 973, 943, 0, 656, 933, 425, 946, 357, 480, 1005, 726, 0, 0, 548, 0, 381, 837, 0, 165, 871, 0, 0, 685, 816, 0, 1138, 521, 877, -1, 0, 0, 512, 0, 0, 165, 949, 0, 0, 0, 0, 1025, 901, 0],[0, 147, 0, 607, 673, 0, 0, 0, 453, 304, 584, 0, 220, 0, 0, 508, 0, 0, 0, 437, 385, 501, 0, 383, 0, 0, 0, 367, 0, 657, 0, 541, 0, -1, 242, 0, 360, 163, 552, 461, 796, 0, 0, 526, 0, 0, 0],[0, 0, 0, 355, 915, 0, 857, 2968, 0, 0, 0, 0, 42, 813, 0, 750, 754, 0, 707, 571, 0, 0, 0, 0, 877, 671, 851, 0, 0, 0, 0, 0, 0, 242, -1, 0, 590, 0, 565, 0, 1000, 0, 1037, 0, 802, 585, 0],[0, 59, 843, 0, 1005, 450, 0, 0, 0, 443, 729, 0, 75, 0, 229, 654, 647, 476, 690, 559, 325, 0, 0, 0, 0, 629, 0, 0, 0, 735, 126, 692, 512, 0, 0, -1, 519, 0, 608, 540, 0, 713, 980, 668, 693, 0, 0],[0, 499, 0, 0, 1684, 635, 421, 0, 0, 208, 316, 278, 0, 404, 0, 244, 369, 83, 359, 319, 0, 821, 470, 587, 0, 206, 0, 0, 713, 612, 0, 244, 0, 360, 590, 519, -1, 428, 0, 0, 454, 571, 0, 0, 0, 0, 0],[485, 142, 0, 1535, 0, 0, 762, 490, 0, 286, 0, 0, 205, 724, 0, 625, 0, 0, 511, 0, 0, 583, 0, 534, 0, 0, 0, 516, 555, 0, 183, 649, 0, 163, 0, 0, 428, -1, 0, 0, 0, 788, 0, 506, 730, 570, 0],[894, 0, 0, 0, 903, 1006, 233823, 587, 945, 0, 0, 311, 593, 0, 0, 0, 938, 0, 358, 0, 923, 988, 202, 935, 0, 467, 556, 0, 0, 0, 0, 0, 165, 552, 565, 608, 0, 0, -1, 0, 0, 0, 797, 430, 1012, 932, 731],[0, 572, 0, 0, 1959, 258, 0, 0, 0, 0, 386, 0, 614, 262, 532, 0, 0, 523, 829, 0, 395, 0, 792, 264, 246, 681, 825, 185, 0, 196, 0, 0, 949, 461, 0, 540, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 511],[1047, 0, 0, 0, 419, 0, 232579, 368, 824, 524, 0, 559, 996, 0, 1137, 0, 0, 475, 0, 484, 1112, 0, 742, 1033, 826, 331, 175, 695, 1167, 946, 836, 472, 0, 796, 1000, 0, 454, 0, 0, 0, -1, 905, 76, 321, 753, 0, 1041],[0, 0, 529, 1007, 511, 2071, 0, 623, 0, 741, 0, 804, 0, 222, 0, 0, 0, 0, 0, 879, 0, 0, 0, 416, 0, 772, 891, 297, 579, 0, 0, 433, 0, 0, 0, 713, 571, 788, 0, 0, 905, -1, 877, 843, 152, 245, 683],[0, 0, 0, 886, 376, 2341, 631, 386, 0, 567, 499, 0, 0, 0, 1157, 502, 0, 0, 0, 542, 1122, 1291, 0, 1036, 0, 0, 241, 688, 1176, 917, 0, 448, 0, 0, 1037, 980, 0, 0, 797, 0, 76, 877, -1, 379, 724, 886, 1065],[831, 628, 0, 1789, 500, 894, 664, 222, 0, 225, 536, 244, 703, 658, 877, 484, 0, 0, 95, 0, 0, 1026, 0, 838, 0, 0, 0, 566, 0, 885, 0, 458, 0, 526, 0, 668, 0, 506, 430, 0, 321, 843, 379, -1, 710, 0, 0],[530, 0, 0, 1830, 0, 0, 111, 487, 0, 0, 0, 701, 0, 0, 0, 236, 0, 0, 800, 763, 600, 0, 0, 0, 0, 0, 0, 0, 0, 193, 585, 0, 1025, 0, 802, 693, 0, 730, 1012, 0, 753, 152, 724, 710, -1, 277, 0],[254, 0, 1353, 800, 575, 198, 0, 550, 0, 0, 0, 643, 0, 326, 0, 396, 0, 512, 820, 0, 0, 0, 749, 193, 321, 0, 833, 198, 0, 0, 393, 452, 901, 0, 585, 0, 0, 570, 932, 0, 0, 245, 886, 0, 277, -1, 0],[229, 0, 1707, 0, 0, 367, 764, 679, 0, 550, 0, 557, 155, 0, 106, 693, 0, 566, 803, 0, 0, 0, 0, 0, 0, 0, 914, 506, 0, 0, 206, 0, 0, 0, 0, 0, 0, 0, 731, 511, 1041, 683, 1065, 0, 0, 0, -1]]



    min_distance = np.zeros((node_no,), dtype=float)  # distances with starting node as min_distance[i]
    travel_route = [[] for y in range(0, node_no)]
    parents = [[0 for x in range(0, node_no)] for y in range(0, node_no)]

    print("Prim's mst:")
    for start_node in range(0, node_no):
        parents[start_node] = primAlgo(start_node, node_no, graph)
    
    cntVisited = 0
    
    # For each mst with a start_node
    for start_node, parent in enumerate(parents):
        print("\nStartnode:" + str(start_node))
        print()
        travel_route[start_node].append(start_node)
        
        # For each node in a specific mst, find the travel route
        index = 1
        while index < node_no:
            lst = []
            for node, parent_node in enumerate(parent):
                if in_travel_route(parent_node, travel_route[start_node]) and not in_travel_route(node, travel_route[start_node]):
                    lst.append(node)
                    index = index + 1
            for l in lst:
                travel_route[start_node].append(l)
                cntVisited += 1

        # Find distance of travel route
        prev_node = start_node
        cur_node = -1
        for i in range(1, node_no):
            cur_node = travel_route[start_node][i]
            if graph[prev_node][cur_node] <= 0:
                min_distance[start_node] = float('inf')
            else:
                min_distance[start_node] = min_distance[start_node] + graph[prev_node][cur_node]
            print("from " + str(prev_node) + " to " + str(cur_node) +" distance: " + str(graph[prev_node][cur_node]))
            prev_node = cur_node

        if graph[cur_node][start_node] <= 0:
            min_distance[start_node] = float('inf')
        else:
            min_distance[start_node] = min_distance[start_node] + graph[cur_node][start_node]

    print("Prim's heuristic:")
    [shortest_min_distance, shortest_travel_route] = find_best_route(node_no, travel_route, min_distance)

    return shortest_min_distance, shortest_travel_route, cntVisited


def primAlgo(start_node, node_no, graph):
    keys = [float('inf') for x in range(0, node_no)]
    parent = [-1 for x in range(0, node_no)]

    unvisited = np.ones((node_no,), dtype=int)  # all nodes are unvisited
    keys[start_node] = 0

    iteration = 1
    while check_unvisited_node(unvisited) and iteration < node_no:
        # Find the unvisited node with minimum key
        min_key_val = sys.maxsize
        min_node = node_no
        for index, key_val in enumerate(keys):
            if unvisited[index] == 1 and key_val < min_key_val:
                min_key_val = key_val
                min_node = index

        unvisited[min_node] = 0

        # Update adjacent nodes
        for node, val in enumerate(keys):
            if keys[node] > graph[min_node][node] > 0 and unvisited[node] == 1:
                keys[node] = graph[start_node][node]
                parent[node] = min_node

        iteration = iteration + 1

    print_mst(parent, node_no, graph)

    return parent


def print_mst(parent, node_no, graph):
    print("Edge \tWeight")
    for i in range(0, node_no):
        print(parent[i], "-", i, "\t", graph[i][parent[i]])


if __name__ == '__main__':
    
    numberCities = 10
    generateTSPInstance(numberCities) 
    
    xLst = []
    y1Lst = []
    y2Lst = []
    
    for numberCities in range(10, 30):
        graph = [[random.randint(0, 10) for i in range(numberCities)]  
                        for j in range(numberCities)]
        startTime = time.time()
        shortest_min_distance, shortest_travel_route, cntVisited = AstarMST(numberCities, graph)
        elapsedTime = time.time() - startTime
        print ("elapsedTime: ", elapsedTime, cntVisited)
        xLst.append(numberCities)
        y1Lst.append(cntVisited)
        y2Lst.append(elapsedTime)
        
    plotXY(xLst, y1Lst, "Number of cities", "Number of nodes expanded", "figure1_NumberofNodeExpanded.pdf")
    
    plotXY(xLst, y2Lst, "Number of cities", "Computation time (s)", "figure2_computationTime.pdf")
