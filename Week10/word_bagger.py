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
    bag = dict()
    text_set = set()
    local_set = set()
    for filename in os.listdir('.\\'):

        #print (file_counter)
        if filename.endswith(".json"): 
         
            with open(filename) as data_file:  
                file_counter += 1
                json_object = json.load(data_file)
                #print(data[4]["title"])
                for data in json_object:
                    # now song is a dictionary
                    if 'body' not in data:
                        data.pop
                    elif 'topics' not in data:
                        data.pop
                    else:                      
                        #print (topic)
                        body = (data['body']).lower()
                        body = re.sub(r"[^\w.,?!]", " ", body)
                        body = re.sub(' +',' ', body)
                        #words = body.split(' ')
                        #for word in words:
                        #   local_set.add(word)
                        #for word in words:
                        #    text_set.add(word)
                        #print (body)
                        texts.append(body)
                        c+=1
                        
                       
        else:
            continue

    print (c)
    print (file_counter)
    print (len(text_set))
    #create_bag_of_words(texts)
    verctorize_bag_of_words(texts)

def create_bag_of_words(texts):
    bagsofwords = [collections.Counter(re.findall(r"[^\w.,?!]", txt)) for txt in texts]
    sumbags = sum(bagsofwords, collections.Counter())
    print (len(sumbags))

def verctorize_bag_of_words(texts):
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(texts) 
    array = X.toarray()
    print (numpy.shape(array))
    featurenames = vectorizer.get_feature_names()
    #print (featurenames)
bag_the_words()