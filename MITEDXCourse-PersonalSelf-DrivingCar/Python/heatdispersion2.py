#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 14:38:50 2019

@author: reality
"""

import numpy as np

def evolve(u):
    temp = np.copy(u)
    mainMatrix = temp[1:-1,1:-1]
    mainMatrix = mainMatrix + 1/4*temp[1:-1, :-2]#Left Border
    mainMatrix = mainMatrix + 1/4*temp[1:-1, 2:]#Right Border
    mainMatrix = mainMatrix + 1/4*temp[0:-2, 1:-1] #Top Border
    mainMatrix = mainMatrix + 1/4*temp[2:, 1:-1] #Bottom Border
    mainMatrix = mainMatrix - temp[1:-1, 1:-1]
    temp[1:-1,1:-1] = mainMatrix    
    print(temp)
    return np.asarray(temp)
    
    


input = np.array([[0.47, 0.26, 0.48, 0.7 ],
                  [0.95, 0.89, 0.43, 0.92],
                  [0.85, 0.64, 0.54, 0.98],
                  [0.17, 0.08, 0.01, 0.48],
                  [0.98, 0.15, 0.96, 0.42]])
"""
Anwser is 
[0.47  , 0.26  , 0.48  , 0.7   ],
[0.95  , 0.57  , 0.7075, 0.92  ],
[0.85  , 0.59  , 0.515 , 0.98  ],
[0.17  , 0.2425, 0.515 , 0.48  ],
[0.98  , 0.15  , 0.96  , 0.42  ]
   """ 
evolve(input)



"""
    Copy222
        temp = np.copy(u)
    mainMatrix = temp[1:-1, 1:-1]
    #print(mainMatrix)
    square = len(temp) == len(temp[0])
    print(square)
    horzMiddle = int(len(u[0]) /2)
    vertMiddle = int(len(u)/2)
    print(square)
    if square == True:
        #print(temp[0:-vertMiddle+1,1:-1])
        mainMatrix = mainMatrix +  0.25*temp[vertMiddle:,1:-1];
        mainMatrix = mainMatrix +  0.25*temp[1:-1,0:horzMiddle+1];
        mainMatrix = mainMatrix +  0.25*temp[1:-1,horzMiddle:];
        mainMatrix = mainMatrix +  0.25*temp[0:vertMiddle+1,1:-1] 
        temp[1:-1,1:-1] = mainMatrix
        print(temp)
        return np.asarray(temp)
    else:
        mainMatrix = mainMatrix +  0.25*temp[vertMiddle+1:,1:-1];
        mainMatrix = mainMatrix +  0.25*temp[1:-1,0:horzMiddle+1];
        mainMatrix = mainMatrix +  0.25*temp[1:-1,horzMiddle:];
        mainMatrix = mainMatrix +  0.25*temp[0:vertMiddle,1:-1] 
        temp[1:-1,1:-1] = mainMatrix
        #print(temp)
        return np.asarray(temp)
    Copy222



    Copy111
    
    temp = np.copy(u)
    temp[1:-1,1] = temp[1:-1,0] + temp[1:-1,1] #left border
    temp[1:-1,-2] = temp[1:-1,-1] + temp[1:-1,-2] #right border
    temp[1,1:-1] = temp[0,1:-1]+temp[1,1:-1]; #top border
    temp[-2,1:-1] = temp[-1,1:-1] + temp[-2,1:-1]#bottom border
    temp[1:-1,1:-1] = temp[1:-1,1:-1]/ 4;
    print(temp)
    return np.asarray(temp)
    
    111

    temp = np.copy(u)
    vert = len(u)
    horz = len(u[0])
    temp[:,1] = temp[:,0] + temp[:,1] #left border
    temp = reset(temp,u)
    temp[:,horz-2] = temp[:,horz-1] + temp[:,horz-2] #right border
    temp = reset(temp,u)
    temp[1] = temp[0] + temp[1];
    temp = reset(temp,u)
    temp[vert-2] = temp[vert-1] + temp[vert-2]
    temp = reset(temp,u) 
    temp = temp/4;
    temp = reset(temp,u)
    return np.asarray(temp)

def reset(temp, u):
    vert = len(u)
    horz = len(u[0])
    temp[0] = u[0]
    temp[vert-1] = u[vert-1]
    temp[:,0] = u[:,0]
    temp[:,horz-1] = u[:,horz-1]
    return temp;
    
 """

