# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 23:05:34 2017

@author: tadah
"""
import json
import pandas as pd
import os
import collections, re
from sklearn.feature_extraction.text import CountVectorizer
import numpy

def bag_the_words():
    c = 0
    file_counter = 0
    texts = []
    for filename in os.listdir('.\\'):
        file_nr = ""
        print (file_counter)
        if filename.endswith(".json"): 
            # print(os.path.join(directory, filename))
            if file_counter < 10:
                file_nr = "00" + str(file_counter)
            else:
                file_nr = "0" + str(file_counter)
            with open('reuters-'+ file_nr+'.json') as data_file:    
                print('reuters-'+ file_nr+'.json')
                json_object = json.load(data_file)
                #print(data[4]["title"])
                for data in json_object:
                    # now song is a dictionary
                    if 'body' not in data:
                        data.pop
                    elif 'topics' not in data:
                        data.pop
                    else:
                        body = data['body']
                        body = re.sub(r"\W", " ", body)
                        body = re.sub(' +',' ',body)
                        texts.append(body)
                        c+=1
            file_counter += 1
            continue
        else:
            continue
    print (c)
    #create_bag_of_words(texts)
    verctorize_bag_of_words(texts)

def create_bag_of_words(texts):
    bagsofwords = [ collections.Counter(re.findall(r'\w+', txt)) for txt in texts]
    sumbags = sum(bagsofwords, collections.Counter())
    print (len(sumbags))

def verctorize_bag_of_words(texts):
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(texts) 
    array = X.toarray()
    print (numpy.shape(array))
    featurenames = vectorizer.get_feature_names()
    #print featurenames
bag_the_words()