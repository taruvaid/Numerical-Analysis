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
z = [[1],[1],[1]]
A = pd.DataFrame(A)
b = pd.DataFrame(b)
z = pd.DataFrame(z)

def jacobi_method(A,b,K,z):
    '''Solving a linear system given by Ax=b using the Jacobi Iterative method
    Applicable for square matrices with onon zero diagonal elements
    K = number of iterations
    z=correct solution of linear system'''
    
    n = A.shape[0] #size of matrix
    x = pd.DataFrame(np.zeros((n,1)))
    e = pd.DataFrame(np.zeros((n,1))) #error
    e_max  = 1
    
    table = [[0,0,0,0,1,1]]
    table = pd.DataFrame(table, columns=['Iteration', 'x1','x2','x3','e_max','e_ratio'])
    
    #start iterations
    for k in range(0,K):
        k+=1
        
        e_max_old = e_max 
        
        #result stores output value of x for iterantions
        for i in range(0,n):
            sum = 0
            for j in range(0,n):
                if i!=j:
                   sum += A.iloc[i,j]*x.iloc[j,0]
            x.iloc[i,0]= (b.iloc[i,0] - sum )/A.iloc[i,i]
            
       
        e = z-x
        
        #infinity norm on one column matrix
        e_max = abs(e.iloc[0,0])
        for i in range(0,n-1):             
            if e_max > abs(e.iloc[i+1,0]):
                print('emax is larger',e_max)
            else:
                e_max = abs(e.iloc[i+1,0])
            
        e_ratio =    e_max/e_max_old
        print ("iteration : ",k)
        print(x)
        
        print("error")
        print(e)
        
        print("e infinity norm")
        print(e_max)
        
        print("e infinity norm ratios")
        print(e_ratio)
        
        df = [[k,x.iloc[0,0],x.iloc[1,0],x.iloc[2,0],e_max,e_ratio]]
        df = pd.DataFrame (df,columns=['Iteration', 'x1','x2','x3','e_max','e_ratio'])
        table = pd.concat([table,df],axis=0)
        
    return x,e,table
       
    
x, e,table =  jacobi_method(A, b,10,z)
print(table)
          
#compare with wikipedia solution https://en.wikipedia.org/wiki/Jacobi_method

#### GAUSS-SEIDAl METHOD


#### SOR - Sucessive Overrelaxation Method
#w= 8 - 3 (7^0.5)

