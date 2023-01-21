# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 16:11:22 2020

@author: abdka
"""
from BinaryTree import BinaryTree
from BinaryTreeNode import BinaryTreeNode
from collections import namedtuple

def dot_visualization(g):
    from graphviz import Digraph, Source

    def add_nodes_edges(tree, dot=None):
        # Create Digraph object
        if dot is None:
            dot = Digraph()
            dot.node(name=str(id(tree)), label=str(tree.value))

        # Add nodes
        if tree.left:
            dot.node(name=str(id(tree.left)) ,label=str(tree.left.value))
            dot.edge(str(id(tree)), str(id(tree.left)), color='red')
            dot = add_nodes_edges(tree.left, dot=dot)

        if tree.right:
            dot.node(name=str(id(tree.right)) ,label=str(tree.right.value))
            dot.edge(str(id(tree)), str(id(tree.right)), color='green')
            dot = add_nodes_edges(tree.right, dot=dot)

        return dot

    # Add nodes recursively and create a list of edges
    dot = add_nodes_edges(g)

    # Visualize the graph
    return dot
                  
def visualize(tree):
    dot = dot_visualization(tree._root)
    dot.render('test-output/test2.gv', view=True)
    

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


binarytree = BinaryTree()
content =  ['F', 'D', 'I', 'B', 'E', 'H', 'M' ,'A' ,'L' ,'X']
for p in content:
    binarytree.insert(value = p)
size = len(content)

visualize(binarytree2)