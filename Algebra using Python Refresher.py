# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 09:19:20 2024

@author: tvaid
"""

#### Solving for x
# homogenous form : ax + b - c = 0. Many functions require this form

import sympy as sym
from IPython.display import display,Math

x = sym.symbols('x')
expr = 2*x + 4 - 9 # homogenous expression #implicitly its set to 0
result = sym.solve(expr)
print(result)

display(Math('\\text{ The }'))