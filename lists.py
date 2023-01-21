# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 16:36:27 2020

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
        self.length = 0
        self.head = None
        self.tail = None
        try:
            iter(data)
        except Exception:
            self.head = MyNode(data)
            self.tail = self.head
            self.length += 1
        else:
            for val in data:
                self.append(val)

    
    def __getitem__(self, idx):
        i = 0
        #For aa kunne jobbe med negative index
        if idx < 0:
            idx = self.length + idx
        temp = self.tail
        if idx > self.length - 1:
            raise IndexError
        else:
            while i < idx:
                temp = temp._next
                i += 1
            return temp._data
    
    
    def __setitem__(self, idx, item):
        if idx < 0:
            idx = self.length + idx
        if idx == self.length - 1:
            self.head._data = item
        elif idx > self.length:
            raise IndexError
        else:
            temp, i = self.tail, 0
            while i < idx:
                temp = temp._next
                i += 1
            temp._data = item
    
   
    def __add__(self, list):
        linked_list = MyLinkedList(self[0])
        for item in self:
            linked_list.append(item)
        try:
            iter(list)
        except Exception:
            linked_list.append(list)
        else:
            for item in list:
                linked_list.append(item)
        return linked_list
    
        
    def __delitem__(self, idx):
        item = self[idx]
        if idx < 0:
            idx = self.length + idx
        if idx > self.length - 1:
            raise IndexError
            return
        if self.length == 1:
            self.head = self.tail = ''
        elif idx == self.length - 1:
            self.head = self.head._previous
            self.head._next = None
        elif idx == 0:
            self.tail = self.tail._next
            self.tail._previous = None
        else:
            temp, i = self.tail._next, 1
            while i < idx:
                temp = temp._next
                i += 1
            temp._previous._next = temp._next
            temp._next._previous = temp._previous
        self.length -= 1
        return item
    
    
    def __eq__(self, list):
        if self.length != len(list):
            return False
        i = 0
        while i < self.length:
            if self.__getitem__(i) != list[i]:
                return False
            i += 1
        return True


    def __iter__(self):
        iterable = []
        for i in range(self.length): 
            iterable.append(self[i])
        return iter(iterable)
    
    
    def __len__(self):
        return self.length
    
    
    def __contains__(self, item):
        i = 0
        temp = self.tail
        
        while i < self.length:
            if temp._data == item:
                return True
            temp = temp._next
            i += 1
        return False
    
    
    def __str__(self):
        i, temp = 1, self.tail
        string = '['
        while i < self.length:
            string += str(temp) + ', '
            temp = temp._next
            i += 1
        string += str(temp) + ']'
        return string
    
    
    def append(self, item):
        if self.length == 0:
            self.head = MyNode(item)
            self.tail = self.head
        elif self.length == 1:
            self.head = MyNode(item)
            self.tail._next = self.head
            self.head._previous = self.tail
        else:
            new_node = MyNode(item)
            new_node._previous = self.head
            self.head._next = new_node
            self.head = new_node
        self.length += 1
        
    
    def insert(self, idx, item):
        new_node = MyNode(item)
        i, temp = 0, self.tail
        if idx < 0:
            idx = self.length + idx
        if idx > self.length + 1:
            raise IndexError
        elif idx == 0:
            new_node._next = self.tail
            self.tail._previous = new_node
            self.tail = new_node
        elif idx == self.length:
            new_node._previous = self.head
            self.head._next = new_node
            self.head = new_node
        else:
            while i < idx:
                temp = temp._next
                i += 1
            new_node._previous = temp._previous
            temp._previous = new_node
            new_node._next = temp
        self.length += 1
            
        
a = MyLinkedList([1, 2])

del a[0]


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
        return self[-1]


    def peek(self):
        return self[-1]
    
    
    def pop(self):
        if len(self) == 0:
            raise IndexError
        else:
            item = self[-1]
            del self[-1]
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
    
    
    
    
    
        
    
        
    
        
        
    

    
    