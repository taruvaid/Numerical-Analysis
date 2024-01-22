# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 08:18:42 2024

@author: tvaid
"""

#this file contains list of packages and their version

# pip install numpy==1.23.1
import numpy as np
print("imported numpy as np")
import pandas as pd 
import matplotlib as mlt 

print ('imported functions successfully')

def my_multiply(x,y):
    mysum=x**y
    print("in my_multiply function")
    return mysum

def create_tridiagonal_matrix(n,e):
    N=(2**n)-1
    h=2**(-n)
    A= pd.DataFrame(np.zeros((N,N)))
    F= pd.DataFrame(np.zeros((N,1)))
    for i in range(0,N):
        for j in range(0,N):
            if abs(i-j)>1:
                A.iloc[i,j]=0
            elif i==j:
                A.iloc[i,j]=(2*e+h**2)/(h**2)
            else:
                A.iloc[i,j]=(-e)/(h**2)
        F.iloc[i,0]=2*(i+1)*h+1
    AT=A.transpose()
    print(f"n is {n}, N is {N},e is {e},h is {h}")
    print(A)
    print(F)
    if A.equals(AT):        
        print("Matrix A is symmetric")        
    else:
        print("Matrix A is not symmetric")
      
    return(A,F,N)
