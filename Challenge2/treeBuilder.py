# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 16:35:28 2017

@author: tadah
"""

from anytree import Node, RenderTree

def buildTree():
     with open("id_pid.txt", 'r') as searchfile:
            
            for line in searchfile:
                words = line[:-2]
                words = words.split(' ')
                print (words)
                kk = Node(str(words[0]), parent=str(words[1]))
                #if words[0][0:2] == "t3":
                #    print(words)

buildTree()