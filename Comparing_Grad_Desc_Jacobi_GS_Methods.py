# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#import packages
import numpy as np

#create square matrix
A = np.array([[10,1,2,3,4],[1,9,-1,2,-3],[2,-1,7,3,-5],[3,2,3,12,-1],[4,-3,-5,-1,15]])
b = np.array([[12],[-27],[14],[-17],[12]])
u=np.zeros([len(b),1])

#Checking if the matrix is positive definite
def is_pos_def(x):
    return np.all(np.linalg.eigvals(x) > 0)

print("Matrix A is positive definite - ",is_pos_def(A))

#Gradient Descent Algorithm
def grad_desc (A,b,u):
    
    r = b - np.matmul(A,u)
    r_t = np.transpose(r) #transpose of residual
    
    #for k in range (1,2):
    while (r_t.dot(r)>0.01):        
        #a_num = np.linalg.norm(r,2) #L2 norm
        a = (r_t.dot(r)) / (r_t.dot(A).dot(r))    
        u = u + a*r
        r = b - np.matmul(A,u) #residual
        r_t = np.transpose(r) #transpose of residual
    return(u,r)

u,r = grad_desc (A,b,u)
