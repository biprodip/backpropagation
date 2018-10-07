#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 17:57:04 2018

@author: ukw
"""

def forwardPass(X):
    global Y_H,Y_O;
    Z_H=np.dot(W_IH,X);   # 3x1= (3x2).(2x1)
    Y_H=sigm(Z_H);        #activation # 3x1
    
    Z_O=np.dot(W_HO,Y_H); # 2x1= (2x3).(3x1)
    Y_O=sigm(Z_O);        #activation. # 2x1
    
    return Y_O;           # 2x1
