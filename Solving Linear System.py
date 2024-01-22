# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 06:36:26 2024

@author: tvaid
"""

## This code contains examples of how to solve a system of linear equations
## the problem we are looking at is of the form Ax=B

import numpy as np
import pandas as pd
import functions as ftv
#print(np.cos(90))
#print(np.inf)

#### PROBLEM 4 - tridiagonal matrix

A,F,N = ftv.create_tridiagonal_matrix(2,10**(-3))

B=pd.DataFrame({'a':[1,2,3],'b':[4,5,6],'c':[7,8,9]})
print(B)
def LP_decomp(M_original,N):   
    A = M_original.copy()
    L= pd.DataFrame(np.zeros((N,N)))
    L.iloc[0,0]=1
    p=0
    for i in range(1,N):
        L.iloc[i,p]= A.iloc[i,i-1]/A.iloc[i-1,i-1]
        for j in range(0,N):
            print(f"i : {i}, j : {j}")
            print(A.iloc[i,j], A.iloc[i-1,j],L.iloc[i,p],A.iloc[i-1,j]*L.iloc[i,p])
            A.iloc[i,j]=A.iloc[i,j] - A.iloc[i-1,j]*L.iloc[i,p]
            
        p+=1
    return(L,A)
            
        


l,C = LP_decomp(B,3)



