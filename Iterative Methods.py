# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 09:02:24 2024

@author: tvaid
"""

#Jacobi Method
#Algorithm
# 1. check - diagonal elements of A must not be 0. 
# 2.  If they are 0 then what happens to the code? Conceptually we cannot proceed but lets see what happens to the code
# 3. initialize x_0 <- any initial value, lets say we set all equal to 0
# 4. create L, U and D 
# 5. calculate x_1 
# 6. Check if x_1 satidfies original eqution. If yes then we have the result. If not then stop after k number of iterations
# 7. Stopping criteria


import numpy as np
import pandas as pd 
import matplotlib as mlt 
import math

##Positive Definite Matrix Tests
# https://en.wikipedia.org/wiki/Definite_matrix
# Positive-definite and positive-semidefinite matrices can be characterized in many ways, which may explain the importance of the concept in various parts of mathematics. A matrix M is positive-definite if and only if it satisfies any of the following equivalent conditions.
# M is congruent with a diagonal matrix with positive real entries.
# M is symmetric or Hermitian, and all its eigenvalues are real and positive.
# M is symmetric or Hermitian, and all its leading principal minors are positive.

##JACOBI METHOD

A = [[3,1,0],[1,3,1],[0,1,3]]
b = [[4],[5],[4]]

A = pd.DataFrame(A)
b = pd.DataFrame(b)


def jacobi_method(A,b,K):
    '''Solving a linear system given by Ax=b using the Jacobi Iterative method
    Applicable for square matrices with onon zero diagonal elements
    K = number of iterations'''
    
    n = A.shape[0] #size of matrix
    x = pd.DataFrame(np.zeros((n,1)))
   #result = pd.DataFrame(np.zeros((n,K)))
    
    #create L+ U
    LU = A.copy()
    for i in range(0,n):
        LU.iloc[i,i]=0
    
        #start iterations
    for k in range(0,K):
        k+=1
        
        #result stores output value of x for iterantions
        result= LU.dot(x) + b
    
        for i in range(0,n):
            result.iloc[i,0] =  result.iloc[i,0]/A.iloc[i,i]
            
        x = result
        print ("iternation : ",k)
        print(x)
    return x,LU,result
       
    
    
x,LU, result =  jacobi_method(A, b,10)

#compare with wikipedia solution https://en.wikipedia.org/wiki/Jacobi_method

#### GAUSS-SEIDAl METHOD


#### SOR - Sucessive Overrelaxation Method
#w= 8 - 3 (7^0.5)

