# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 06:36:49 2024

@author: tvaid
"""

import numpy as np
import pandas as pd 
import matplotlib as mlt 
import math




## Code to perform Cholesky factorization...
A = [[4,12,-16],[12,37,-43],[-16,-43,98]]
A = [[2,-1,0,0],[-1,2,-1,0],[0,-1,2,-1],[0,0,-1,2]]
A = [[1,1/2,1/3,1/4],[1/2,1/3,1/4,1/5],[1/3,1/4,1/5,1/6],[1/4,1/5,1/6,1/7]]
A = pd.DataFrame(A)
def cholesky_factorization (A):
    """A = symmetric positive definite matrix
       A = L*Transpose(L)
       Function returns L """
    n=A.shape[0]
    print(f'matrix dimensions {A.shape[0]} x {A.shape[1]}')
    L = pd.DataFrame(np.zeros((n,n)))
    L.iloc[0,0]=math.sqrt(A.iloc[0,0])
    
    for i in range(0,n):
        for j in range(i,n): 
            print(i,j)
            if i==0:
                L.iloc[j,i]= A.iloc[i,j]/L.iloc[0,0]
            elif i==j:
                s=0
                for k in range(0,i):
                    s=s+L.iloc[i,k]**2
                L.iloc[i,i]=math.sqrt(A.iloc[i,i]-s)
            else:
                s=0
                for k in range(0,j):
                    s=s+L.iloc[i,k]*L.iloc[j,k]
                L.iloc[j,i]=(A.iloc[i,j]-s)/L.iloc[i,i] 
                #print(L.iloc[j-1,j-1])
 
    
    return(L,s)


L,s = cholesky_factorization(A)
print(L)
