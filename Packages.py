# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 08:18:42 2024

@author: tvaid
"""

#this file contains list of packages and their version

# pip install numpy==1.23.1
import numpy as np
print("imported numpy as np")
import pandas as pd 
import matplotlib as mlt 

print ('imported requirements successfully')

def my_multiply(x,y):
    mysum=x**y
    print("in my_multiply function")
    return mysum