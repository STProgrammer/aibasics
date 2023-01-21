# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 20:29:42 2020

@author: abdka
"""

def intpow(x, n):
    if n==0:
        return 1
    elif n < 0:
        return 1 / intpow(x, -n)
    else:
        return x * intpow(x, n-1)
    
    

print('3^0 =', intpow(3,0))

print('3^1 =', intpow(3,1))

print('3^3 =', intpow(3,3))

print('4^-1 =', intpow(4, -1))

print('4^-2 =', intpow(4, -2))