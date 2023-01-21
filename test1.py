# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 09:13:21 2020

@author: abdka
"""
from collections import namedtuple
from BinaryTree import BinaryTree 
from BinaryTreeNode import BinaryTreeNode

person = namedtuple('person', ['lastname', 'firstname', 'address',
                                            'postal_code', 'city'])

persons_file2 = open('unbalanced.dta', 'r')
content = persons_file2.read()
content2 = content.splitlines()
size2 = len(content2)
binarytree2 = BinaryTree()
for p in content2:
    binarytree2.insert(value = person(*p.split(';')))
    print(person(*p.split(';')))
persons_file2.close()

value = person(*'MANJOSSOV;UNNI MERETHE;BURSTUEN 85;3535;KRÃ˜DEREN'.split(';'))
print(value)

print("Here is the finding: -------------------")

print(binarytree2.find(value).value)

persons_file1 = open('Personer-kort.dta', 'r')
content = persons_file1.read()
content1 = content.splitlines()
size1 = len(content1)
binarytree1 = BinaryTree()
for p in content1:
    binarytree1.insert(value = person(*p.split(';')))
persons_file1.close()

value = person(*'HUSBY;DAG HELGE;VALDE 32;4353;KLEPP STASJON'.split(';'))
print(value)

print(binarytree1.find(value).value)