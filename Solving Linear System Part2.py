# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 20:03:31 2024

@author: tvaid
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import functions as ftv

#PROBLEM 5
N=4
A,B = ftv.polynomial_matrix(N)

#LU decomposition function takes the Matrix and N as inputs      
L,U = ftv.LP_decomp(A,N)
    
#forward substitution    
y=ftv.forward_subst(L, B, N)

#backward substitution
u=ftv.backward_subst(U,y,N)
        
        
        

