# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 14:30:26 2020

@author: abdka
"""

from collections import namedtuple
import numpy as np
import pandas as pd
from BinaryTree import BinaryTree
from BinaryTreeNode import BinaryTreeNode


btree = BinaryTree()

personrecord = namedtuple('personrecord', ['lastname', 'firstname', 'address', 'postal_code', 'city'])
i = 0

some_persons = list()


for row in pd.read_csv('Personer.dta', delimiter=';', encoding='ANSI', header=None).itertuples():
    person = personrecord(*row[1:])
    btree.insert(value = person)
    i += 1
    if i == 1 or i == 10 or i == 100 or i == 1000 or i == 10000 or i == 100000:
        some_persons.append(person)
        level = btree.find(person).level
        some_persons.append(level)
        print('Row number {0} is: {1}. Its level on tree is: {2} \n'.format(i, person[:], level))


print('The person nr. 1000 and nr 10000:')
pers = btree.find(some_persons[6])
if isinstance(pers, BinaryTreeNode):
    print(pers.value)
else:
    print(pers)

pers = btree.find(some_persons[8])
if isinstance(pers, BinaryTreeNode):
    print(pers.value)
else:
    print(pers)


print('\nDeleting the perons nr 1000 and nr 10000 from Personer.dta:')
pers1 = btree.delete(some_persons[6])
pers2 = btree.delete(some_persons[8])
if isinstance(pers1, BinaryTreeNode):
    print(pers1.value)
else:
    print(pers1)
    
if isinstance(pers2, BinaryTreeNode):
    print(pers2.value)
else:
    print(pers2)

pers = btree.find(some_persons[6])
if isinstance(pers, BinaryTreeNode):
    print(pers.value)
else:
    print(pers)
    
pers = btree.find(some_persons[8])
if isinstance(pers, BinaryTreeNode):
    print(pers.value)
else:
    print(pers)

print('The person nr. 1000 and nr 10000:')
pers = btree.find(some_persons[6])
if isinstance(pers, BinaryTreeNode):
    print(pers.value)
else:
    print(pers)

pers = btree.find(some_persons[8])
if isinstance(pers, BinaryTreeNode):
    print(pers.value)
else:
    print(pers)

print('\nDeleting the perons nr 1000 and nr 10000 from Personer.dta:')
pers1 = btree.delete(some_persons[6])
pers2 = btree.delete(some_persons[8])
if isinstance(pers1, BinaryTreeNode):
    print(pers1.value)
else:
    print(pers1)
    
if isinstance(pers2, BinaryTreeNode):
    print(pers2.value)
else:
    print(pers2)

pers = btree.find(some_persons[6])
if isinstance(pers, BinaryTreeNode):
    print(pers.value)
else:
    print(pers)
    
pers = btree.find(some_persons[8])
if isinstance(pers, BinaryTreeNode):
    print(pers.value)
else:
    print(pers)