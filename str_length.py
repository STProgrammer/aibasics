# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 20:42:09 2020

@author: abdka
"""

"sdfsdfsdfs"



def str_length(string):
    if string == '':
        return 0
    return 1 + str_length(string[1:])


while True:   
    string = input('Type in a string to get its lenght: ')
    
    print('length of the string is: ', str_length(string))

    
    