#installing and importing packages
import numpy as np
import pandas as pd

#Defining the block tridiagonal matrix
B = np.array([[4, -1, 0],
              [-1, 4, -1],
              [0, -1, 4]])

#extract size of B
n = B.shape[0]  

#number of blocks in A
m = 3  

#creating the tridiagonal matrix
A = np.zeros((m*n,m*n))

for i in range(m):
    A[i*n:(i+1)*n, i*n:(i+1)*n] = B
    if i > 0:
        A[i*n:(i+1)*n, (i-1)*n:i*n] = -np.eye(n)
    if i < m-1:
        A[i*n:(i+1)*n, (i+1)*n:(i+2)*n] = -np.eye(n)
        
#initializing b
b = np.array([0, 0, 1, 0, 0, 1, 0, 0, 1])

# Initial value of x
x0 = np.zeros_like(b)

##Jacobi Method
def jacobi_method(A, b, x0, tol=1e-2, max_iter=100):
    n = len(b)
    x = x0.copy()
    residuals = []
    
    for k in range(max_iter):
        x_new = np.zeros_like(x)
        for i in range(n):
            x_new[i] = (b[i] - np.dot(A[i], x) + A[i, i] * x[i]) / A[i, i]
        
        #https://numpy.org/doc/stable/reference/generated/numpy.linalg.norm.html
        residual = np.linalg.norm(b - np.dot(A, x_new), ord=1)
        residuals.append(residual)
        
        if residual < tol:
            break
        
        x = x_new
    
    return k + 1, residuals[-1], residuals[-1] / residuals[-2] if len(residuals) > 1 else np.nan


# Solving using Jacobi method
k_jacobi, residual_jacobi, ratio_jacobi = jacobi_method(A, b, x0)
print("Using Jacobi Method:")
print("Iterations performed (k):", k_jacobi)
print("Residual at final stage (kr(k)k1):", residual_jacobi)
print("Ratio of successive residual norms at final stage:", ratio_jacobi)


# Gauss-Seidel method function
def gauss_seidel_method(A, b, x0, tol=1e-2, max_iter=100):
    n = len(b)
    x = x0.copy()
    residuals = []
    
    for k in range(max_iter):
        for i in range(n):
            x[i] = (b[i] - np.dot(A[i, :i], x[:i]) - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]
        
        residual = np.linalg.norm(b - np.dot(A, x), ord=1)
        residuals.append(residual)
        
        if residual < tol:
            break
    
    return k + 1, residuals[-1], residuals[-1] / residuals[-2] if len(residuals) > 1 else np.nan


# Solving using GS method
k_gs, residual_gs, ratio_gs = gauss_seidel_method(A, b, x0)
print("\nGauss-Seidel Method:")
print("Iterations performed (k):", k_gs)
print("Residual at final stage (kr(k)k1):", residual_gs)
print("Ratio of successive residual norms at final stage:", ratio_gs)