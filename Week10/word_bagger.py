# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 23:05:34 2017

@author: tadah
"""
import json
import pandas as pd

def bag_the_words():
    print("doing stuff")
   # pd.json.loads("C:\\Users\\tadah\\Documents\\BigDataExercises\\Week10\\reuters-010.json")
    with open('C:\\Users\\tadah\\Documents\\BigDataExercises\\Week10\\reuters-010.json') as data_file:    
        data = json.load(data_file)
        print(data[4]["title"])

bag_the_words()