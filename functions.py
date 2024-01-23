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

## create a tridiagonal matrix
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

## LU decomposition
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
#forward substitution - parameters L = lower triangular matriz, F= output values , N = matrix size
def forward_subst(L,F,N):
    y= pd.DataFrame(np.zeros((N,1)))
    y.iloc[0]= F.iloc[0]
    for i in range(0,N):
        j=0  
        s=0
        while j<i:        
           s = s+ y.iloc[j]*L.iloc[i,j]
           j+=1
        y.iloc[i]=F.iloc[i]-s
    
    return(y)


#backward substitution - parameters U = upper traingular matrix (diagonal not necessarily 1),
#y = result from Ly=F, and N = size of matrix
def backward_subst(U,y,N):
    x= pd.DataFrame(np.zeros((N,1)))
    x.iloc[N-1]= y.iloc[N-1]/U.iloc[N-1,N-1]
    i=N-2
    while i>=0:        
        j=N-1
        s=0
        while j>i:        
           s = s+ x.iloc[j]*U.iloc[i,j]
           j-=1
        x.iloc[j]=(y.iloc[i]-s)/U.iloc[i,j]
        i-=1
        
    
    return(x)
#function to create a matrix for polynial p(t)=a0 + a1t+a1t^2...a(n-1)t^(n-1)
def polynomial_matrix(N):
    A= pd.DataFrame(np.zeros((N,N)))
    B= pd.DataFrame(np.zeros((N,1)))
    for i in range(0,N):
        for j in range(0,N): 
            A.iloc[i,j]=(2+i)**(j)
        B.iloc[i,0]=((2+i)**N -1)/(i+1)
    return(A,B)