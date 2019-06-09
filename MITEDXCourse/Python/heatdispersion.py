#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 14:38:50 2019

@author: reality
"""

import numpy as np

def evolve(u):
    temp = np.copy(u)
    #finalAnswer = np.asarray([])
    finalAnswer = np.asarray(temp[0])
    
    vertAmount = len(u)
    horzAmount = len(u[0])
    for i in range(1,vertAmount-1):
        #for each row here
        firstIndex = temp[i,0];
        array = [firstIndex]
        for z in range(1,horzAmount-1):
            sum = temp[i+1,z] + temp[i-1,z] + temp[i,z+1] + temp[i, z-1];
            sum = sum/4
            array.append(sum)
        array.append(temp[i,horzAmount-1])
        #print(array
        finalAnswer = np.append(finalAnswer, np.asarray(array));
    
    finalAnswer = np.append(finalAnswer, temp[vertAmount-1])
    finalAnswer = np.split(finalAnswer, vertAmount)
    
    print(finalAnswer)
    return np.asarray(finalAnswer)
    


input = np.array([[100, 100, 100, 100, 100],
 [100,   0,   0,   0, 100],
 [100, 100, 100, 100, 100]])

evolve(input)


