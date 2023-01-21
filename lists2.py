# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 12:27:22 2020

@author: abdka
"""

class MyNode: 
    def __init__(self, dataval, previosval=None, nextval=None):
        self._previous = previosval
        self._next = nextval
        self._data = dataval
    
    
    def __str__(self):
        return str(self._data)
    
    

class MyLinkedList:
    def __init__(self, data):
        self.list = []
        try:
            iter(data)
        except Exception:
            self.list.append(data)
        else:
            for val in data:
                self.append(val)

    
    def __getitem__(self, idx):
        return self.list[idx]
    
    
    def __setitem__(self, idx, item):
        self.list[idx] = item
    
   
    def __add__(self, list):
        newlist = self.list
        try:
            iter(list)
        except Exception:
            newlist.append(list)
        else:
            newlist += list
        return newlist
    
        
    def __delitem__(self, idx):
            del self.list[idx]


    def __eq__(self, list):
        return self.list == list


    def __iter__(self):
        return iter(self.list)
    
    
    def __len__(self):
        return len(self.list)
    
    
    def __contains__(self, item):
        if item in self.list:
            return True
        else:
            return False
    
    
    def __str__(self):
        return str(self.list)
    
    
    def append(self, item):
        self.list.append(item)
        
    
    def insert(self, idx, item):
        self.list.index(idx, item)
        
        
        
a = MyLinkedList([1, 2])

print(a)


class MyStack(MyLinkedList):
    
    #MyLinkedList can't initialized being empty, but
    #MyStack should be initialized with empty data,
    #so I make a custom initialization function
    
    def __init__(self):
        super(MyStack, self).__init__(1)
        del self[0]
    
    
    def push(self, data):
        self.append(data)
    
    
    def top(self):
        return self.list[len(self.list - 1)]


    def peek(self):
        return self.list[len(self.list - 1)]
    
    
    def pop(self):
        if len(self.list) == 0:
            raise IndexError
        else:
            item = self.list[-1]
            del self.list[-1]
            return item



class MyFIFO(MyLinkedList):
    def __init__(self):
        super(MyFIFO, self).__init__(1)
        del self[0]
    
    
    def enqueue(self, object):
        self.append(object)
    
    
    def dequeue(self):
        if len(self) == 0:
            raise IndexError
        item = self[0]
        del self[0]
        return item
    


#Test MyFIFO
fifo = MyFIFO()

fifo.enqueue('a')
fifo.enqueue('b')
fifo.enqueue('c')

print('Initial FIFO')

print(fifo)


print('\nElements taken from FIFO:')
print(fifo.dequeue())
print(fifo.dequeue())
print(fifo.dequeue())

print('\nStack after elements are popped:')
print(fifo)

fifo.enqueue('z')

print(fifo.dequeue())



#Test MyStack
stack = MyStack()

# append() function to push
# element in the stack

stack.push('a')
stack.push('b')
stack.push('c')

print('Initial stack')

print(stack)

# pop() function to pop
# element from stack in

# LIFO order
print('\nElements popped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())

print('\nStack after elements are popped:')
print(stack)

stack.push('z')

print(stack.pop())

# uncommenting print(stack.pop()) should cause an IndexError as the stack is now empty 
