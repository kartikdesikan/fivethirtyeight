# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 17:19:11 2018

@author: kartik
"""
#Simulating https://fivethirtyeight.com/features/where-will-the-seven-dwarfs-sleep-tonight/

import random
import time
import pandas as pd
import numpy as np

random.seed(time.time())
simulations = pow(10,6)
#n should be at least 2
n = 7

start = time.clock()
def sim():
    i = 1
    lst = [None] * n
    elements = list(range(1,n+1))
    positions = list(range(1,n+1))
    while (i <=n):
        #print(i)
        #print("E:",elements)
        #print("P:",positions)
        #Special condition for dwarf 1
        if i==1:
            pos = random.randint(2,n)   
        else:
            #If a dwarf find his bed free
            if lst[i-1] == None:
                pos = i
            else:
                pos = positions[random.randint(1,len(positions))-1]
        #print("pos:",pos)
        lst[pos-1] = i
        #print("lst:",lst)        
        elements.remove(i)
        positions.remove(pos)
        i = i+1
    return lst
combined = []
#print(sim())
combined = [sim() for _ in range(simulations)]
df = pd.DataFrame.from_records(combined, columns=list(range(1,n+1)))

#What is the probability that the oldest dwarf sleeps in his own bed?
print("Probability that the oldest dwarf sleeps in his own bed: %f"%((df[n]==n).sum()/simulations))

#What is the expected number of dwarfs who do not sleep in their own beds?
exp_df = pd.DataFrame()
for i in range(1,n+1):
        exp_df[i] = (df[i]!=i)
print("Expected number of dwarfs who do not sleep in their own beds: %f"%(np.mean(exp_df.sum(axis=1))))

print("Time taken to run %d simulations:%f seconds"%(simulations,time.clock()-start))

