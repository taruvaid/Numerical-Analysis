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

#A= ftv.create_tridiagonal_matrix(2,10**(-3))


def create_tridiagonal_matrix(n,e):
    N=(2**n)-1
    h=2**(-n)
    A= pd.DataFrame(np.zeros((N,N)))
    F= pd.DataFrame(np.zeros((N,1)))
    for i in range(0,N):
        for j in range(0,N):
            if abs(i-j)>1:
                A[i][j]=0
            elif i==j:
                A[i][j]=(2*e+h**2)/(h**2)
            else:
                A[i][j]=(-e)/(h**2)
        F[i]=9
    AT=A.transpose()
    print(f"n is {n}, N is {N},e is {e},h is {h}")
    print(A)
    if A.equals(AT):        
        print("Matrix is symmetric")        
    else:
        print("Matrix is not symmetric")
      
    return(A,F)


#A,F=create_tridiagonal_matrix(2,1)
F= pd.DataFrame(np.zeros((3,1)))
F[0][0]=9
F[0][1]=9

df=pd.DataFrame({'name':["clarke","robin","betty","betty"],
            'marks1':[10,20,30,40],
            'marks2':[30,40,50,60]})

df[0,1]