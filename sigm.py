#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 17:59:02 2018

@author: ukw
"""

def sigm(Z):
    # activation function 
    return 1/(1+np.exp(-Z)); #same dimension as Z