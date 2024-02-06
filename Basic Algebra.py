# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 14:46:53 2024

@author: tvaid
"""

##Solve for x
import sympy as sym
from IPython.display import display,Math

x=sym.symbols('x')
expr = 2*x + 4 -9 #implicitly equation set to 0 in sympy
result = sym.solve(expr)
print(result)