# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 06:36:26 2024

@author: tvaid
"""

## This code contains examples of how to solve a system of linear equations
## the problem we are looking at is of the form Ax=B

import numpy as np
import pandas as pd
import functions as ftv


#### PROBLEM 4 - tridiagonal matrix

#B=pd.DataFrame({'a':[1,2,11,12],'b':[4,5,6,7],'c':[7,8,9,10],'d':[10,11,12,13]})
#print(B)

A,F,N = ftv.create_tridiagonal_matrix(2,10**(-3))        
L,U = ftv.LP_decomp(A,N)



