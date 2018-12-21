#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 18:00:13 2018

@author: biprodip
"""

def error(T,Y):
    # squared loss function 
    return  np.square(T-Y) ; #same dimension as Y
