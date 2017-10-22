# -*- coding: utf-8 -*-
"""
Created on Thu Oct 05 11:34:50 2017

@author: Emil
"""

def kmp(t, p):
    if t is None or p is None:
        return ''
    n = len(t)
    m = len(p)
    
    for i in range(n-m+1):
        for j in range (m):
            if t[i+j] != p[j]:
                break            
        if j==m:
            print i

kmp("i have a really nice cat in hat at home", "cat" )