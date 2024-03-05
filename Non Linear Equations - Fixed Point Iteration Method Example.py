# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 22:46:37 2024

@author: tvaid
"""

import numpy as np

#f(x) = x^3 - x + 1
#g(x) = x 
# where g(x) = x^3 +1 or (x-1)^(1/3)

def f(x):
    return x**3 - x + 1

# def g(x):
#     return (x - 1) ** (1/3)

def g(x):
    return x - f(x) / 3  # Choose M = 3

def fpim(g, x0, tolerance=1e-15, max_iterations=1000):
    x = x0
    for _ in range(max_iterations):
        x_next = g(x)
        if abs(x_next - x) < tolerance:
            return x_next
        x = x_next
    raise ValueError("Fixed-point iteration method did not converge.")

# Initial guess
x0 = -1.5

# Apply fixed-point iteration method with the chosen function g(x)
try:
    result_fpim = fpim(g, x0)
    print(f" Fixed point iteration method : root is {result_fpim}")
except ValueError as e:
    print(e)



