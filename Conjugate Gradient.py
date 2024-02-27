# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 05:29:57 2024

@author: tvaid
"""

#import packages
import numpy as np

#create square matrix
n = 32
A = np.zeros([n,n])
b = np.zeros([n,1])
u = np.zeros([n,1])

for row in range(0,n):
    for col in range(0,n):
        A[row,col] = 1/ (1 + (row + 1) + (col + 1))
        b[row,0] = b[row,0] + A[row,col]
    b[row,0] = b[row,0]/3
    

#Checking if the matrix is positive definite
def is_pos_def(x):
    return np.all(np.linalg.eigvals(x) > 0)

print("Matrix A is positive definite - ",is_pos_def(A))

#Conjugate Gradient
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


#Gradient Descent Algorithm
def grad_desc (A,b,u,e):
    """Solving a linear system Au=b
    error = e"""
    
    r = b - np.matmul(A,u)
    r_t = np.transpose(r) #transpose of residual
    
    counter = 0 
    
    #for k in range (1,20000):
    while (r_t.dot(r)>e):    
        
        counter+=1
        
        #a_num = np.linalg.norm(r,2) #L2 norm
        a = (r_t.dot(r)) / (r_t.dot(A).dot(r))    
        u = u + a*r
        r = b - np.matmul(A,u) #residual
        r_t = np.transpose(r) #transpose of residual
    return(u,r,counter)

u_gd,r_gd,c_gd = grad_desc (A,b,u,0.00001)
u_cg,c_cg = conj_grad(A,b,u,0.00001)

print(f"No of iterations of gradient descent are {c_gd}; while for conjugate gradient are {c_cg}")
