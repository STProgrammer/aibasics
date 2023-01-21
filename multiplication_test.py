# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 20:25:55 2020

@author: abdka
"""

import matplotlib.pyplot as plt
import timeit


CODE1 = '''import random 
small_numbers = [random.randint(1, 10) for _ in range(101)]'''

CODE2 = '''
import random
medium_numbers = [random.randint(10**5, 10**6) for _ in range(101)]'''

CODE3 = '''
import random
big_numbers = [random.randint(10**10, 10**11) for _ in range(101)]'''

CODE4 = '''
import random
xxl_numbers = [random.randint(10**15, 10**16) for _ in range(101)]'''

timerecords = [
    timeit.timeit(setup=CODE1, 
                  stmt='[small_numbers[i] * small_numbers[i+1] for i in range(100)]'),
    timeit.timeit(setup=CODE2, 
                  stmt='[medium_numbers[i] * medium_numbers[i+1] for i in range(100)]'),
    timeit.timeit(setup=CODE3, 
                  stmt='[big_numbers[i] * big_numbers[i+1] for i in range(100)]'),
    timeit.timeit(setup=CODE4, 
                  stmt='[xxl_numbers[i] * xxl_numbers[i+1] for i in range(100)]')]

integer_sizes = [1, 5, 10, 15]

print(timerecords)

plt.scatter(integer_sizes, timerecords)
plt.title("Multiplication of two numbers 100 times each in python and recorded time")

plt.ylabel("seconds")
plt.xlabel("integer size in digits")

plt.ylim(ymin=0)

plt.show()






