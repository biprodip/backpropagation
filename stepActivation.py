#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 01:38:42 2018

@author: biprodip
"""

def stepActivation(X,W):
    import numpy as np

    #computed decision on step function
    # IF WX>0  1  else  0
    D=np.ones(X[0].shape);
    D[(W.dot(X))<0]=0;
    return D