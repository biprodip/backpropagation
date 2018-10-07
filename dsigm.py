#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 17:59:42 2018

@author: ukw
"""

def dsigm(Y):
    # derivative of sigmoid function 
    return Y * (1-Y) ; #same dimension as Y