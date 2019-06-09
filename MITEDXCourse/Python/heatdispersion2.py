#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 14:38:50 2019

@author: reality
"""

import numpy as np
import time;
def evolve(u):
    start= time.time()
    temp = np.copy(u)
    vert = len(u)
    horz = len(u[0])
    print(u)
    temp[1:vert-1,1] = temp[1:vert-1,0] + temp[1:vert-1,1] #left border
    temp[1:vert-1,horz-2] = temp[1:vert-1,horz-1] + temp[1:vert-1,horz-2] #right border
    temp[1][1:horz-1] = temp[0][1:horz-1]+temp[1][1:horz-1]; #top border
    temp[vert-2][1:horz-1] = temp[vert-1][1:horz-1] + temp[vert-2][1:horz-1]#bottom border
    temp[1:vert-1,1:horz-1] = temp[1:vert-1,1:horz-1]/ 4;
    print(temp)
    end = time.time()
    print(end-start)
    return np.asarray(temp)



input = np.array([[100, 100, 100, 100, 100],
                            [100,   0,   0,   0, 100],
                            [100, 100, 100, 100, 100]])

evolve(input)



"""
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

