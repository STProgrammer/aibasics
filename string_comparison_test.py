# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 18:21:16 2020

@author: abdka
"""

import timeit

print('''We will test how long it takes to compare two strings of different sizes,
doing comparisons with these cases:
    * two strings with same size where only last letter is different
    * two strings with different size where only last letter is different
    * two strings with same size, first letter is different
    * two strings with different size, first letter is different
We will make teste with two strings two times for each case, first
we will compare two strings of sizes 1000 characters and in second case
we will compare two strings of sizes 1000,000 characters and compare
how long it takes to compare strings when string size increases in the
four cases described above. Each comparesin will be repeated 1000 times
to get enough data.\n''')


print('''\nWorst case : two strings with same size where only last letter is different
trying from 1001 to 1000001 characters long of strings:''')

CODE ='''
string1 = ''.join(["a" for _ in range(1000)])
string2 = ''.join(["a" for _ in range(999)]) + "b"
'''
print(timeit.timeit(setup=CODE, stmt="string1==string2", number=1000))


CODE ='''
string1 = ''.join(["a" for _ in range(1000000)])
string2 = ''.join(["a" for _ in range(999999)]) + "b"
'''

print(timeit.timeit(setup=CODE, stmt="string1==string2", number=1000))



print('''\nTwo strings with different size where only last letter is different:''')

CODE ='''
string1 = ''.join(["a" for _ in range(1000)])
string2 = ''.join(["a" for _ in range(1000)]) + "b"
'''
print(timeit.timeit(setup=CODE, stmt="string1==string2", number=1000))


CODE ='''
string1 = ''.join(["a" for _ in range(1000000)])
string2 = ''.join(["a" for _ in range(1000000)]) + "b"
'''

print(timeit.timeit(setup=CODE, stmt="string1==string2", number=1000))



print('''\nNow we test the best scnearios.
Two strings with same size, first letter is different''');

CODE ='''
string1 = ''.join(["a" for _ in range(1000)])
string2 = ''.join(["b" for _ in range(1000)])
'''

print(timeit.timeit(setup=CODE, stmt="string1==string2", number=1000))


CODE ='''
string1 = ''.join(["a" for _ in range(1000000)])
string2 = ''.join(["b" for _ in range(1000000)])
'''

print(timeit.timeit(setup=CODE, stmt="string1==string2", number=1000))



print('''\nNow we test the best scnearios.
Two strings with different size, first letter is different''');


CODE ='''
string1 = ''.join(["a" for _ in range(1000)])
string2 = ''.join(["b" for _ in range(1001)])
'''

print(timeit.timeit(setup=CODE, stmt="string1==string2", number=1000))


CODE ='''
string1 = ''.join(["a" for _ in range(1000000)])
string2 = ''.join(["b" for _ in range(1000001)])
'''

print(timeit.timeit(setup=CODE, stmt="string1==string2", number=1000))




print('''\nIn worst scneario it looks like higher than O(n)
in best scenario it looks like less than O(logn). When the
first letter is different or size is different, the number of
characters doesn't matter much, but in wors case scenario it's like O(n)''')







