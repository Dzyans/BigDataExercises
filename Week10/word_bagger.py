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

import numpy as np


from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification

def bag_the_words():
    c = 0
    file_counter = 0
    texts = []
    topics = []
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
                        texts.append(body)
                        if 'earn' in data['topics']:                            
                            topics.append(1)
                        else:
                            topics.append(0)
                        c+=1
                        
                       
        else:
            continue

    print (c)

    return verctorize_bag_of_words(texts), topics

def verctorize_bag_of_words(texts):
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(texts) 
    array = X.toarray()
    #print (numpy.shape(array))
    featurenames = vectorizer.get_feature_names()
    #print (len(featurenames))
    return X 
    
    
def randomtree(X, y):
    clf = RandomForestClassifier(max_depth=2, random_state=0, n_estimators=50, n_jobs = 2)
    Xarray = X.toarray()
    
    y = np.asarray(y)
   
    
    trainX = Xarray[:8300]
    trainY = y[:8300]
    
    testX = Xarray[8301:]
    testy = y[8301:]
    print (testy.ravel())
    print("testX "+  str(len(testX)))
    print("testy " + str(len(testy)))
    
    clf.fit(trainX , trainY)
    
    #RandomForestClassifier(bootstrap=True, class_weight=None, criterion='gini',
     #       max_depth=20, max_features='auto', max_leaf_nodes=None,
      #      min_impurity_decrease=0.0, min_impurity_split=None,
       #     min_samples_leaf=1, min_samples_split=2,
        #    min_weight_fraction_leaf=0.0, n_estimators=500, n_jobs=2,
         #   oob_score=False, random_state=0, verbose=0, warm_start=False)
    
   
    
    print (clf.feature_importances_)
    predictions = clf.predict(testX)
    print ("number of predictions " + str(len(predictions)))
    pos = 0
    neg = 0
    
    for i in range(0, len(testy)):
        if predictions[i] == testy[i]:
           pos += 1 
        else:
            neg += 1
    
    print ("negetives "+ str(neg))
    
    print ("positives "+ str(pos))
    
    print ("correctness ratio " +  str(pos / len(testy)))

X,y = bag_the_words()

print (len(y))
print (y[:5])
randomtree(X, y)