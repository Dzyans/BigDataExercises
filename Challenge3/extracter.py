# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 12:49:03 2017

@author: s123725
"""

import zipfile
with open('videos.zip', 'rb') as MyZip:
  print(MyZip.read(4))

#with zipfile.ZipFile("videos.zip","r") as zip_ref:
#    zip_ref.extractall("videos")