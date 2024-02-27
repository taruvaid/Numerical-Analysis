# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
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

u,r,c = grad_desc (A,b,u,0.001)
print(u)
print(c)