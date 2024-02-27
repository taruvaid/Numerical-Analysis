# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#import packages
import numpy as np
import pandas as pd

#create square matrix
A = np.array([[10,1,2,3,4],[1,9,-1,2,-3],[2,-1,7,3,-5],[3,2,3,12,-1],[4,-3,-5,-1,15]])
b = np.array([[12],[-27],[14],[-17],[12]])
u=np.zeros([len(b),1])
z= np.array([[1],[-2],[3],[-2],[1]])

#pandas dataframes
A_df = pd.DataFrame(A)
b_df= pd.DataFrame(b)
u_df = pd.DataFrame(u)
z_df = pd.DataFrame(z)

#Checking if the matrix is positive definite
def is_pos_def(x):
    return np.all(np.linalg.eigvals(x) > 0)

print("Matrix A is positive definite - ",is_pos_def(A))


##### Gradient Descent Algorithm
def grad_desc (A,b,u):
    c=0
    r = b - np.matmul(A,u)
    r_t = np.transpose(r) #transpose of residual
    
    #for k in range (1,2):
    while (r_t.dot(r)>0.0001):
        c+=1        
        #a_num = np.linalg.norm(r,2) #L2 norm
        a = (r_t.dot(r)) / (r_t.dot(A).dot(r))    
        u = u + a*r
        r = b - np.matmul(A,u) #residual
        r_t = np.transpose(r) #transpose of residual
    return(u,r,c)

u_gd,r,c_gd = grad_desc (A,b,u)

#### Jacobi Method
def jacobi_method(A,b,K):
    '''Solving a linear system given by Ax=b using the Jacobi Iterative method
    Applicable for square matrices with onon zero diagonal elements
    K = number of iterations
    z=correct solution of linear system'''
    
    n = A.shape[0] #size of matrix
    x = pd.DataFrame(np.zeros((n,1)))
        
    
    #create L+ U
    LU = A.copy()
    for i in range(0,n):
        LU.iloc[i,i]=0
    
        #start iterations
    for k in range(0,K):
        k+=1
                
        #result stores output value of x for iterantions
        result= -LU.dot(x) + b
    
        for i in range(0,n):
            result.iloc[i,0] =  result.iloc[i,0]/A.iloc[i,i]
            
        x = result.copy()
        
    return x,LU
    
u_jacobi,LU =  jacobi_method(A_df, b_df,22)

#### Gauss - Seidal Method
def gauss_seidal_method(A,b,K):
    '''Solving a linear system given by Ax=b using the Jacobi Iterative method
    Applicable for square matrices with onon zero diagonal elements
    K = number of iterations
    z=correct solution of linear system'''
    
    n = A.shape[0] #size of matrix
    x = pd.DataFrame(np.zeros((n,1)))
 
    #start iterations
    for k in range(0,K):
        k+=1
                   
        #result stores output value of x for iterantions
        for i in range(0,n):
            sum = 0
            for j in range(0,n):
                if i!=j:
                   sum += A.iloc[i,j]*x.iloc[j,0]
            x.iloc[i,0]= (b.iloc[i,0] - sum )/A.iloc[i,i]
            
    return x
           
u_gs =  gauss_seidal_method(A_df, b_df,22)

#### Conjugate Gradient
def conj_grad(A,b,u,e):
    """ Solving linear system Ax = b 
    u = starting point
    e = error
    """
    r = b - np.matmul(A,u)
    r_t = np.transpose(r) #transpose of residual
    d = -r
    d_t = -r_t
    counter = 0 
    
    #for k in range (1,5):
    while (r_t.dot(r)>e): 
        
        counter+=1
        
        #alpha
        a = (r_t.dot(d)) / (d_t.dot(A).dot(d)) 
        
        #descent method with direction d(k)
        u = u + a*d
        
        #re-calculating residuals
        r = b - np.matmul(A,u)
        r_t = np.transpose(r)
        
        #beta
        bt = (r_t.dot(A).dot(d)) / (d_t.dot(A).dot(d)) 
        
        #new descent direction
        d = -r+ bt*d
        d_t = np.transpose(d)
        
        print("loop - ", counter,"- residuals")
        print(r)
        
    return u,counter
u_cg, c_cg = conj_grad(A, b, u, 0.0001)

print("Conjugate Gradient  Solution vs Actual Soln")
print(u_cg - z)

print("Jacobi Solution vs Actual Soln")
print(u_jacobi - z_df)
print("GSMethod Solution vs Actual Soln")
print(u_gs - z_df)
print("Gradient Descent Solution vs Actual Soln")
print(u_gd - z)

print(f'Iterations of  gradeint descent {c_gd}' )
print(f'Iterations of conjugate gradeint {c_cg}' )


##conclusion
## GD takes 22 iterations to get to a result. However GS gets us a more accurate result. 
## GD seems quite fast (especially in the problem with large value of A), however accuracy can be improved