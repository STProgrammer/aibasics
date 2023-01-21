# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 07:24:17 2020

@author: abdka
"""

import graphviz
from mybinarynode import MyBinaryNode


prefix = input("Please enter a prefix expression: ")

prefix2 = '+ + * 4 5 6 7'
binary_expression = MyBinaryNode.inputPrefix(prefix)

binary_expression.visualize()
print('\nThe infix form is: ', end='')
binary_expression.infixOrder()
print('\nThe postfix form is: ', end='')
binary_expression.postfixOrder()
print('\nThe result is: ', binary_expression.calculate())





'''
prefix2 = '+ + 1 2 + 3 4'
binary_expression = MyBinaryNode.inputPrefix(prefix2)

print('\nThe infix form is: ', end='')
binary_expression.infixOrder()
print('\nThe postfix form is: ', end='')
binary_expression.postfixOrder()
print('\nThe result is: ', binary_expression.calculate())

prefix2 = '+ + 1 2 3 + 4'
binary_expression = MyBinaryNode.inputPrefix(prefix2)

print('\nThe infix form is: ', end='')
binary_expression.infixOrder()
print('\nThe postfix form is: ', end='')
binary_expression.postfixOrder()
print('\nThe result is: ', binary_expression.calculate())

prefix2 = '+ + + 1 2 3 4'
binary_expression = MyBinaryNode.inputPrefix(prefix2)

print('\nThe infix form is: ', end='')
binary_expression.infixOrder()
print('\nThe postfix form is: ', end='')
binary_expression.postfixOrder()
print('\nThe result is: ', binary_expression.calculate())
'''