# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 06:36:26 2024

@author: tvaid
"""

## This code contains examples of how to solve a system of linear equations
## the problem we are looking at is of the form Ax=B

import Packages
ages = Packages.np.array([10,12,13,14])

import numpy as np
print(np.cos(90))
print(np.inf)

#pandas warmup
import pandas as pd
df=pd.DataFrame({'name':["clarke","robin","betty"],
            'marks':[10,20,30]})

#the following statements are identical
print(df.marks[2])
print(df['marks'][2])
print(df.loc[2,'marks'])
print(df.T) ##transpose


#### PROBLEM 4 - tridiagonal matrix
def create_matrix(N):
    A= pd.DataFrame(np.zeros((N,N)))
    for i in range(0,N):
        for j in range(0,N):
            if abs(i-j)>1:
                A[i][j]=0
            else:
                A[i][j]=99
    return(A)

A= create_matrix(5)
#A= pd.DataFrame(np.zeros((3,3)))
#A[0][0]=99

