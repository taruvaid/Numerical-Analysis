# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 09:02:24 2024

@author: tvaid
"""

#Jacobi Method
#Algorithm
1. check - diagonal elements of A must not be 0. 
2.  If they are 0 then what happens to the code? Conceptually we cannot proceed but lets see what happens to the code
3. initialize x_0 <- any initial value, lets say we set all equal to 0
4. create L, U and D 
5. calculate x_1 
6. Check if x_1 satidfies original eqution. If yes then we have the result. If not then stop after k number of iterations
7. Stopping criteria
