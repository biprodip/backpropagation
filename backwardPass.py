#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 17:57:54 2018

@author: ukw
"""

def backwardPass(X,T, Y_O, Y_H):
    global W_HO,W_IH;
    DEL_OUT = (T-Y_O)*dsigm(Y_O); #2x1
    DEL_W_OH = np.dot(DEL_OUT,Y_H.T); #2x3= (2x1).((3x1).T)
    
    DEL_HI = np.dot(W_HO.T,DEL_OUT)*dsigm(Y_H); #3x1= ( (2x3).T . (2x1))  x (3x1))
    DEL_W_HI = np.dot(DEL_HI, X.T); # 3x2 = (3x1) . (2x1).T 
    
    W_HO = W_HO + (eta_ho * DEL_W_OH);  #2x3= (2x3) + (2x3)
    W_IH = W_IH + (eta_ih * DEL_W_HI);  #3x2= (3x2) + (3x2)
    
    return 0;