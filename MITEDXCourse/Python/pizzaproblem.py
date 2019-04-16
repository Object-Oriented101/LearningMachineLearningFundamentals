#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 13:12:01 2019

@author: reality
"""

def cost_calculator(*args, **kwargs):
    totalCost = 0;
    toppingsCount = [];
    drinksCount = [];
    wingsCount = [];
    couponCount = 0;
    pizzaCount = 0;
    for i in kwargs:
        if i == "drinks":
            if kwargs[i] != None:
                drinksCount = kwargs[i]
        elif i == "coupon":
             if kwargs[i] != None:
                 couponCount = kwargs[i]
        elif i == "wings":
             if kwargs[i] != None:
                 wingsCount = kwargs[i]
    
    #sum of the drinks
    if drinksCount != []:
        for i in drinksCount:
            if i == "small":
                totalCost += 2;
            if i == "medium":
                totalCost += 3;
            if i == "large":
                totalCost += 3.5;
            if i == "tub":
                totalCost += 3.75;
                
    if wingsCount != []:
        for i in wingsCount:
            if i == 10:
                totalCost += 5;
            if i == 20:
                totalCost += 9; 
            if i == 40:
                totalCost += 17.5;   
            if i == 100:
                totalCost += 48;

    if len(args) != 0:
        for i in args:
            if i == []:
                print("HERE")
                pizzaCount += 1;
            elif i[0] == "pepperoni" or i[0] == "mushroom" or i[0] == "olive" or i[0] == "anchovy" or i[0] == "ham":
                print("here2")
                pizzaCount+= 1;
                toppingsCount.append(i)
        totalCost += pizzaCount * 13;
    
    print(len(toppingsCount))
    if len(toppingsCount) != 0:
        for z in toppingsCount:
            for i in z:
                print("lkajsfjlsad",i)
                if i == "pepperoni":
                    totalCost += 1;
                elif i == "mushroom":
                    totalCost += 0.5
                elif i == "olive":
                    totalCost += 0.5
                elif i == "anchovy":
                    totalCost += 2
                elif i == "ham":
                    totalCost += 1.5
                else:
                    print("NOTHING")
    print(totalCost)
    off = totalCost*couponCount
    totalCost += totalCost*6.25/100
    totalCost = totalCost - off
    return round(totalCost, 2)
    
    
cost_calculator(['mushroom'], ['anchovy', 'anchovy'], drinks=None, wings=None)
"""
pizzaCount = 0;
    toppingsCount = [];
    drinksCount = [];
    wingsCount = 0;
    couponCount = 0;
    
    #Takes in the input
    for i in args:
        if i == []:
            pizzaCount += 1;
        if i[0] == "small" or i[0] == "medium" or i[0] == "large":
            print("HERE")
            drinksCount.append(i)
            
            """