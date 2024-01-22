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

#A,F,N = ftv.create_tridiagonal_matrix(2,10**(-3))

B=pd.DataFrame({'a':[1,2,11,12],'b':[4,5,6,7],'c':[7,8,9,10],'d':[10,11,12,13]})
print(B)
def LP_decomp(M_original,N):   
    U = M_original.copy()
    L= pd.DataFrame(np.zeros((N,N)))
    L.iloc[0,0]=1
    for p in range(0,N-1):
        for i in range(p+1,N):
            print(f'p =={p}')
            print(U,"\n")
            L.iloc[i,p]= U.iloc[i,p]/U.iloc[p,p]
            L.iloc[i,i]=1
            for j in range(0,N):
                print(f"i : {i}, j : {j}")
                print("parameter values - ")
                print(U.iloc[i,j], U.iloc[i-1,j],L.iloc[i,p],U.iloc[i-1,j]*L.iloc[i,p],"\n")
                U.iloc[i,j]=U.iloc[i,j] - U.iloc[p,j]*L.iloc[i,p]
                
                
    return(L,U)
            
        


L,U = LP_decomp(B,4)



