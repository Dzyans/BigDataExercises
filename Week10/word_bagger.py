# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 23:05:34 2017

@author: tadah
"""
import json
import pandas as pd
import os

def bag_the_words():
    #print("doing stuff")
    # pd.json.loads("C:\\Users\\tadah\\Documents\\BigDataExercises\\Week10\\reuters-010.json")
    c = 0
    for filename in os.listdir('.\\'):
        if filename.endswith(".json"): 
            # print(os.path.join(directory, filename))
            with open('reuters-010.json') as data_file:    
                json_object = json.load(data_file)
                #print(data[4]["title"])
                for data in json_object:
                    # now song is a dictionary
                    if 'body' not in data:
                        data.pop
                    elif 'topics' not in data:
                        data.pop
                    else:
                        c+=1
            continue
        else:
            continue
    print c
   
bag_the_words()