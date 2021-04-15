# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 00:17:17 2020

@author: jackb
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

probList = []
#Set starting probability
startProb = .02

#Set average win rate
winRate = .4    #This is win percentage not ratio win/loss, a ratio of 1 is a rate of .5

#Create current probability variable
currentProb = startProb

#Set change rates
changeWin = .02     
changeLoss = .015

n = 1  # number of rolls, probability of each trial
numGames = 100000


for i in range(numGames):
    gameResult = np.random.binomial(n, winRate)
    if gameResult == 1:
        roll = np.random.binomial(n, currentProb)
        if roll == 1:
            currentProb = startProb
            probList.append(currentProb)
        else:
            currentProb += changeWin
            probList.append(currentProb)
    else:
        currentProb += changeLoss
        probList.append(currentProb)
    if i == 50:
        print(probList)
       
df=pd.DataFrame({'x': [i for i in range(numGames)], 'Probability': probList})
 
#line plot
plt.plot( 'x', 'Probability', data=df, marker='', color='blue', linewidth=2)