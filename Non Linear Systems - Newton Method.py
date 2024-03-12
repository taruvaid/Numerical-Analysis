# -*- coding: utf-8 -*-
"""
Created on Thu Mar 07 21:24:52 2024

@author: tvaid
"""

## Newton's Method - Non Linear Systems
import numpy as np
import functions as ftv
import pandas as pd
import openpyxl
import numpy as np
import matplotlib.pyplot as plt

# Define the functions f, g, and h
def f(x, y, z):
    return x + y + z

def g(x, y, z):
    return x**2 + y**2 + z**2 - 2

def h(x, y, z):
    return x*(y + z) + 1

# Function for Jacobian matrix of the system
def jacobian(x, y, z):
    return np.array([[1, 1, 1],
                     [2*x, 2*y, 2*z],
                     [y + z, x, x]])

# Define the system of equations as a function
def system_equations(vars):
    x, y, z = vars
    return [f(x, y, z), g(x, y, z), h(x, y, z)]

# Function for Newton's method
def newtons_method(func, jacobian, initial_guess, steps):
    x = np.array(initial_guess, dtype=float)
    residuals = []
    for _ in range(steps):
        fx = np.array(func(x), dtype=float)
        residuals.append(fx)
        J = jacobian(*x)
        delta = np.linalg.solve(J, -fx)
        x += delta
    return x, np.array(residuals)

# Initial guess
initial_guess = [3/4, 1/2, -1/2]

# Computing approximation and residuals for 2, 4, and 8 steps
steps_list = [2, 4, 8]
results = {}
for steps in steps_list:
    root, residuals = newtons_method(system_equations, jacobian, initial_guess, steps)
    results[steps] = {'root': root, 'residuals': residuals}

# Consolidated results
print("Step\tRoot\t\tResiduals")
for steps, data in results.items():
    print(f"{steps}\t{data['root']}\t{data['residuals'][-1]}")
