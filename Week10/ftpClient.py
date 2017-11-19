# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 16:01:39 2017

@author: tadah
"""

import requests
from os import getcwd


def download_all():

    for i in range (0,21):   
        nr = ""
        if i >= 10:
            nr = "" + str(i)
        else:
            nr = "0" + str(i)
        url = "https://raw.githubusercontent.com/fergiemcdowall/reuters-21578-json/master/data/full/reuters-0" + nr + ".json"
        #url = "https://raw.github.com/someguy/brilliant/master/somefile.txt"
        directory = getcwd()
        filename = directory + '\\reuters-0' + nr + '.json'
        r = requests.get(url)
        content = bytearray(r.content)
        print (len(content))
        print (filename)
        f = open(filename,'wb')
        f.write(content)
        f.close()
        
download_all()

