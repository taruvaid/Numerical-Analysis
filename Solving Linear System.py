# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 06:36:26 2024

@author: tvaid
"""

## This code contains examples of how to solve a system of linear equations
## the problem we are looking at is of the form Ax=B

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import functions as ftv


#### PROBLEM 4 - tridiagonal matrix

#B=pd.DataFrame({'a':[1,2,11,12],'b':[4,5,6,7],'c':[7,8,9,10],'d':[10,11,12,13]})
#print(B)
n=8
e=10**(-3)
#matrix function takes n and e as inputs
A,F,N = ftv.create_tridiagonal_matrix(n,e)  

#LU decomposition function takes the Matrix and N as inputs      
L,U = ftv.LP_decomp(A,N)
    
#forward substitution    
y=ftv.forward_subst(L, F, N)

#backward substitution
u=ftv.backward_subst(U,y,N)

##graph
x=pd.DataFrame(np.zeros((N,1)))
for i in range(0,N):    
    x.iloc[i]=(i+1)*(2**(-n))
    
plt.scatter(x,u,color='red')




