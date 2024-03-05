# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 19:48:53 2024

@author: tvaid
"""

#import packages
import numpy as np
import pandas as pd
from IPython.display import Math,display


#define function sqr_root
def sqr_root(a, initial_guess, tolerance=1e-6, max_iterations=1000):
    t = initial_guess
    for _ in range(max_iterations):
        t_next = 0.5 * (t + a / t)
        if abs(t_next - t) < tolerance:
            break
        t = t_next
    return t



#define function cubic root
def cubic_root(a, initial_guess, tolerance=1e-6, max_iterations=1000):
    t = initial_guess
    for _ in range(max_iterations):
        t_next = (2 * t + a / (t * t)) / 3
        if abs(t_next - t) < tolerance:
            break
        t = t_next
    return t

#define function quadratic root
def qua_root(a, initial_guess, tolerance=1e-6, max_iterations=250):
    t = initial_guess
    for _ in range(max_iterations):
        t_next = (3 * t + a / (t * t * t)) / 4
        if abs(t_next - t) < tolerance:
            break
        t = t_next
    return t

#Main for square_root
a = 25
initial_guess = 1  # Initial point
sqrt_a = sqr_root(a, initial_guess)
print("Square root of", a, "is approximately:", sqrt_a)

# Main for cubic root:
a = 8
initial_guess = 1.5
cubic_rt = cubic_root(a, initial_guess)
print("Cubic root of", a, "is approximately:", cubic_rt)

# Main for quartic root:
a = 27
initial_guess = 2.5
qua_rt = qua_root(a, initial_guess)
print("Quadratic root of", a, "is approximately:", qua_rt)


## BISECTION Method
def f(x, n,z):
    return x**n - z  # Generalized function for finding nth root of z

def bisection(a, b, n,z, steps):
    for step in range(steps):
        c = (a + b) / 2
        if f(c, n,z) == 0 or (b - a) / 2 < 1e-15:
            return c
        elif f(c, n, z) * f(a, n, z) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2

a = 1
b = 2
n = 3  # For cubic root
z = 5
steps = 10

result_bisection = bisection(a, b, n,z , steps)
print(f" Bisection Method : {n}th root of {z} is {result_bisection}")

##REGULA FALSI

def regula_falsi(a, b, n,z, steps):
    for step in range(steps):
        c = (a * f(b, n,z) - b * f(a, n,z)) / (f(b, n,z) - f(a, n,z))
        if f(c, n,z) == 0:
            return c
        elif f(c, n,z) * f(a, n,z) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2

a = 1
b = 2
n = 3  # For cubic root
steps = 10
z = 5

result_regula_falsi = regula_falsi(a, b, n, z, steps)
print(f" Regula Falsi : {n}th root of {z} is {result_regula_falsi}")

##Fixed Point Iteration Method

#function f(x)
def f(x):
    return x**3 - 5

#function g1(x)
def g1(x):
    return x - f(x)/16

#function g2(x)
def g2(x):
    if x == 0:
        return float('inf')
    return 5 / (x**2)

def fpim(g, x0, tolerance=1e-15, max_iterations=1000):
    x = x0
    for _ in range(max_iterations):
        x_next = g(x)
        if abs(x_next - x) < tolerance:
            return x_next
        x = x_next
    raise ValueError("The fixed-point iteration did not converge.")

# Initial value
t0 = 1.5

# Using g1(x)
result_fpim_g1 = fpim(g1, t0)
print(f" Fixed Point Iteration Method using g1 : {n}th root of {z} is {result_fpim_g1}")


# Using g2(x)
# try:
#     result_fpim_g2 = fpim(g2, t0)
#     print(f" Fixed Point Iteration Method using g2 : {n}th root of {z} is {result_fpim_g2}")
# except ValueError as e:
#     print(e)

## Newton Method
def f(x, n, z):
    return x**n - z

def f_prime(x, n):
    return n * x**(n-1)

def newton_method(x0, n,z, tolerance=1e-15, max_iterations=1000):
    x = x0
    for _ in range(max_iterations):
        x_next = x - f(x, n,z) / f_prime(x, n)
        if abs(x_next - x) < tolerance:
            return x_next
        x = x_next
    raise ValueError("Newton's method did not converge.")

# Initial value and n (degree of the root)
x0 = 1.5
n = 3  # For cubic root
z = 5
try:
    result_nm = newton_method(x0, n,z)
    print(f" Newton Method : {n}th root of {z} is {result_nm}")
except ValueError as e:
    print(e)

#### Secant Method
def f(x):
    return x**3 - 5

def secant_method(x0, x1, tolerance=1e-15, max_iterations=1000):
    for _ in range(max_iterations):
        fx0 = f(x0)
        fx1 = f(x1)
        if abs(fx1) < tolerance:
            return x1
        x_next = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
        x0, x1 = x1, x_next
    raise ValueError("Secant method did not converge.")

# Initial values
t0 = 1.5
t1 = 2

try:
    result_sm = secant_method(t0, t1)
    print(f" Secant Method  : {n}th root of {z} is {result_sm}")
except ValueError as e:
    print(e)
    




