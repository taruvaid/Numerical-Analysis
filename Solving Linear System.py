# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 06:36:26 2024

@author: tvaid
"""

## This code contains examples of how to solve a system of linear equations
## the problem we are looking at is of the form Ax=B


import numpy as np
import pandas as pd
#print(np.cos(90))
#print(np.inf)

#### PROBLEM 4 - tridiagonal matrix
def create_tridiagonal_matrix(N,e,h):
    A= pd.DataFrame(np.zeros((N,N)))
    
    for i in range(0,N):
        for j in range(0,N):
            if abs(i-j)>1:
                A[i][j]=0
            elif i==j:
                A[i][j]=(2*e+h^2)/(h**2)
            else:
                A[i][j]=(-e)/(h**2)
    AT=A.transpose()
    print(f"Nis {N},e is {e},h is {h}")
    print(A)
    if A.equals(AT):        
        print("Matrix is symmetric")        
    else:
        print("Matrix is not symmetric")
      
    return(A)
A= create_tridiagonal_matrix(5,1,2)
n=4
L = [[0.0] * n for i in range(n)]


