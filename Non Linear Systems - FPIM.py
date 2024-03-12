# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 19:51:54 2024

@author: tvaid
"""

import numpy as np
import functions as ftv
import pandas as pd
import openpyxl
import numpy as np
import matplotlib.pyplot as plt

# functions g1 and g2
def g1(x1, x2):
    return (x1**2 + x2**2 + 8) / 10

def g2(x1, x2):
    return (x1*(x2**2) + x1 + 8) / 10

# fixed-point iteration method
def fixed_point_iteration(g1, g2, initial_guess, tol=1e-6, max_iter=100):
    x1, x2 = initial_guess
    for _ in range(max_iter):
        x1_new, x2_new = g1(x1, x2), g2(x1, x2)
        if np.abs(x1_new - x1) < tol and np.abs(x2_new - x2) < tol:
            return x1_new, x2_new
        x1, x2 = x1_new, x2_new
    return x1_new, x2_new

# Initial guess
initial_guess = (0.7, 1.0)

# Perform fixed-point iteration
result = fixed_point_iteration(g1, g2, initial_guess)

# Solution 
print("Solution using FIPM :", result)
