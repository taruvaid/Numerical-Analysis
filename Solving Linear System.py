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
#print(np.cos(90))
#print(np.inf)

#### PROBLEM 4 - tridiagonal matrix

#A= ftv.create_tridiagonal_matrix(2,10**(-3))



A,F=ftv.create_tridiagonal_matrix(2,1)

