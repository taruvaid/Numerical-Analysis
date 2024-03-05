# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 22:38:21 2024

@author: tvaid
"""

def f(x):
    return x**3 - x + 1

def f_prime(x):
    return 3*x**2 - 1

def newton_method(x0, tolerance=1e-15, max_iterations=1000):
    x = x0
    for _ in range(max_iterations):
        fx = f(x)
        if abs(fx) < tolerance:
            return x
        x_next = x - fx / f_prime(x)
        if abs(x_next - x) < tolerance:
            return x_next
        x = x_next
    raise ValueError("Newton's method did not converge.")

# Initial guess
x0 = 1.0

# Stopping criterion (tolerance)
tolerance = 1e-10

try:
    result_nm = newton_method(x0, tolerance)
    print(f" Newton Method  : root is {result_nm}")
except ValueError as e:
    print(e)
