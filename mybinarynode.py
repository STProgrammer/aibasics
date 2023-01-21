# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 09:02:00 2020

@author: abdka
"""

class MyBinaryNode:
    def __init__(self, value,
                 lefttree = None,
                 righttree = None):
        self.value = value
        self.left = lefttree
        self.right = righttree
    
    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, value):
        self.__value = value
    
    @property
    def left(self):
        return self.__left
    
    @left.setter
    def left(self, lefttree):
        self.__left = lefttree
    
    @property
    def right(self):
        return self.__right
    
    @right.setter
    def right(self, righttree):
        self.__right = righttree
    
    
    def __eq__(self, node):
        if node == None:
            return False
        elif not isinstance(node, MyBinaryNode):
            raise Exception("Equality are only for object of equal types")
        else:
            return self.value == node.value
    
    def __str__(self):
        return self.value
    
    def hasRight(self):
        return self.right != None
    
    def hasLeft(self):
        return self.left != None
    
    def info(self):
        retval = self.value + " : ( "
        if isinstance(self.right, MyBinaryNode):
            retval += self.right.value +" )"
        else:
            retval += "none )"
        return retval
        
    
    def prefixOrder(self):
        print(self, ' ', end = '')
        if self.hasLeft():
            self.left.prefixOrder()
        if self.hasRight():
            self.right.prefixOrder()
    
    def infixOrder(self):
        if self.hasLeft():
            print('(', end = '')
            self.left.infixOrder()
            print(' ', end = '')
        print(self, end = '')
        if self.hasRight():
            print(' ', end = '')
            self.right.infixOrder()
            print(')', end = '')
    
    
    def operate(self, operand1, operator, operand2):
        operand1 = int(operand1)
        operand2 = int(operand2)
        if operator == '+':
            return operand1 + operand2
        elif operator == '*':
            return operand1 * operand2
        elif operator == '/':
            return operand1 / operand2
        elif operator == '-':
            return operand1 - operand2
        elif operator == '^':
            return operand1**operand2
        else:
            return
        
    
    def calculate(self):
        operator = self.value
        if self.hasLeft():
            operand1 = self.left.calculate()
        if self.hasRight():
            operand2 = self.right.calculate()
            result = self.operate(operand1, operator, operand2)
            return result
        return self.value
            
            
    def postfixOrder(self):
        if self.hasLeft():
            self.left.postfixOrder()
        if self.hasRight():
            self.right.postfixOrder()
        print(self, ' ', end = '')


    def levelOrder(self):
        from queue import SimpleQueue
        FIFOQueue = SimpleQueue()
        FIFOQueue.put(self)
        self.levelOrderEntry(FIFOQueue)
        while not FIFOQueue.empty():
            node = FIFOQueue.get()
            print(node, ' ', end='')

    
    def levelOrderEntry(self, queue):
        if queue.empty():
            return
        node = queue.get()
        print(node, ' ', end='')
        if node.hasLeft():
            queue.put(node.left)
        if node.hasRight():
            queue.put(node.right)
        if node.hasLeft() or node.hasRight():
            self.levelOrderEntry(queue)

    @staticmethod
    def __isValid(oplist):
        operatorlist = ['+','-','*','/','^']
        if oplist[0] not in operatorlist or not oplist[-1].isnumeric() or not oplist[-2].isnumeric():
            print("first condition")
            return False
        operators = 0
        operands = 0
        length = len(oplist) - 2
        for i in range(length):
            if oplist[i] in operatorlist:
                operators += 1
            elif not oplist[i].isnumeric():
                raise Exception("Invalid character!")
                return False
            else:
                operands += 1
            if operators < operands:
                print("second condition")
                return False
        if operators != operands + 1:
            print("third condition")
            return False
        return True


    @classmethod
    def inputPrefix(cls, expression):
        oplist = expression.split()
        if len(oplist) == 0:
            return
        if not cls.__isValid(oplist):
            raise Exception("The expression is invalid")
        root = MyBinaryNode(None)
        root = cls.__add(oplist)
        return root
    

    @classmethod
    def __add(cls, oplist):
        if len(oplist) == 0:
            return
        operators = ['+','-','*','/','^']
        root = MyBinaryNode(oplist.pop(0))
        if root.value in operators:
            root.left = cls.__add(oplist)
            root.right = cls.__add(oplist)
            return root
        else:
            return root
    
    def visualize(self):
        import graphviz
        dot = graphviz.Digraph()
        dot.node('root', self.value)
        if self.hasLeft():
            dot.node(str(id((self.left))), self.left.value)
            dot.edge('root', str(id(self.left)))
            self.left.__visualizeRecursion(dot)
        if self.hasRight():
            dot.node(str(id((self.right))), self.right.value)
            dot.edge('root', str(id((self.right))))
            self.right.__visualizeRecursion(dot)
        dot.render('test-output/test.gv', view=True)
        
        
        
    def __visualizeRecursion(self, dot):
        if self.hasLeft():
            dot.node(str(id((self.left))), self.left.value)
            dot.edge(str(id(self)), str(id(self.left)))
            self.left.__visualizeRecursion(dot)
        if self.hasRight():
            dot.node(str(id((self.right))), self.right.value)
            dot.edge(str(id((self))), str(id((self.right))))
            self.right.__visualizeRecursion(dot)
    
    def visualizeTest(self):
        import graphviz
        dot = graphviz.Digraph()
        print(self)
        print(self.left)
        print(self.right)
        dot.node(str(id(self)), self.value)
        dot.node(str(id((self.left))), self.left.value)
        dot.node(str(id((self.right))), self.right.value)
        dot.edge(str(id(self)), str(id(self.left)))
        dot.edge(str(id((self))), str(id((self.right))))
        dot.render('test-output/binarytree.gv', view=True)
        print(dot.source)
        


'''
def inputPrefix(expression):
    oplist = expression.split()
    print(oplist)
    if len(oplist) == 0:
        return
    root = add(oplist)
    return root


def add(oplist):
    if len(oplist) == 0:
        return
    operators = ['+','-','*','/','^']
    root = MyBinaryNode(oplist.pop(0))
    if root.value in operators:
        root.left = add(oplist)
        root.right = add(oplist)
        return root
    else:
        return root
'''
