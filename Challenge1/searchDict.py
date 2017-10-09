# -*- coding: utf-8 -*-
"""
Created on Mon Oct 09 15:23:34 2017

@author: Emil
"""

word = 'cat'
dict = {
    'cat' : 'A1.txt',
    'cate' : 'A2.txt',
    'cateling' : 'A1.txt',
    'bob' : 'A4.txt'
}

def check_dict(word,dict):
    list = []
    
    for key in dict.iterkeys():
        if word not in key:
            continue
        if dict[key] not in list:
            list.append(dict[key])
    return list

print check_dict(word,dict)


