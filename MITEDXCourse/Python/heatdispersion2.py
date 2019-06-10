#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 14:38:50 2019

@author: reality
"""

import numpy as np

def evolve(u):
    temp = np.copy(u)
    mainMatrix = temp[1:-1, 1:-1]
    print(mainMatrix)
    horzMiddle = int(len(u[0]) /2)
    vertMiddle = int(len(u)/2)


    print(temp[0:-vertMiddle+1,1:-1])
    mainMatrix = mainMatrix +  0.25*temp[vertMiddle:,1:-1];
    mainMatrix = mainMatrix +  0.25*temp[1:-1,0:horzMiddle+1];
    mainMatrix = mainMatrix +  0.25*temp[1:-1,horzMiddle:];
    mainMatrix = mainMatrix +  0.25*temp[0:vertMiddle+1,1:-1] 
    temp[1:-1,1:-1] = mainMatrix
    print(temp)
    return np.asarray(temp)



input = np.array([[100, 100, 100, 100, 100],
                            [100,   0,   0,   0, 100],
                            [100,   0,   0,   0, 100],
                            [100,   0,   0,   0, 100],
                            [100, 100, 100, 100, 100]])

evolve(input)



"""
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

