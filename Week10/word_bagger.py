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
import timeit
import numpy as np
import hashlib


from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification

def bag_the_words():
    c = 0
    file_counter = 0
    texts = []
    topics = []
    hashed_features = []
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
                        hashed_array = []
                        hashed_array = hashing_vectorizer(body.split(' '), 1000)
                        hashed_features.append(hashed_array)
                        if 'earn' in data['topics']:                            
                            topics.append(1)
                        else:
                            topics.append(0)
                        c+=1
                        
                       
        else:
            continue

    print (c)
    
    return verctorize_bag_of_words(texts), hashed_features, topics

def create_bag_of_words(texts):
    start_time = timeit.default_timer()
    bagsofwords = [collections.Counter(re.findall(r"[^\w.,?!]", txt)) for txt in texts]
    sumbags = sum(bagsofwords, collections.Counter())
    elapsed = timeit.default_timer() - start_time
    print("Bag_of_words_created_in " + str(elapsed) + " seconds")
    print (len(sumbags))
   

def verctorize_bag_of_words(texts):
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(texts) 
    array = X.toarray()
    #print (numpy.shape(array))
    featurenames = vectorizer.get_feature_names()
    #print (len(featurenames))
    return X 
    
def int_generator(md5_hashed_string):
    value = 0
    counter = 0
    for char in md5_hashed_string:
        value += ord(char) + counter*4242
        counter += 1
    return value

def hashing_vectorizer(features, n_features):
    hashed_features = np.zeros(n_features, dtype=int)
    
    for feature in features:
        #print ("the word is: " + feature)
        hashed = hashlib.md5(feature.encode()).hexdigest()
        
        index = int_generator(hashed) % n_features
        #print ("index " + str(index))
        hashed_features[index] = 1
        #print (hashed_features)
        
        #print (hashed.hexdigest())
    return hashed_features
    
    
def randomtree(X, y):
    
    print ("\n--------------Growing new Tree-----------------")
    start_time = timeit.default_timer()
    clf = RandomForestClassifier(max_depth=2, random_state=0, n_estimators=50, n_jobs = 2)
    
    y = np.asarray(y)
   
    
    trainX = X[:8300]
    trainY = y[:8300]
    
    testX = X[8301:]
    testy = y[8301:]
    
    #print (testy.ravel())
    #print("testX "+  str(len(testX)))
    #print("testy " + str(len(testy)))
    
    clf.fit(trainX , trainY)
    
    #RandomForestClassifier(bootstrap=True, class_weight=None, criterion='gini',
     #       max_depth=20, max_features='auto', max_leaf_nodes=None,
      #      min_impurity_decrease=0.0, min_impurity_split=None,
       #     min_samples_leaf=1, min_samples_split=2,
        #    min_weight_fraction_leaf=0.0, n_estimators=500, n_jobs=2,
         #   oob_score=False, random_state=0, verbose=0, warm_start=False)
    
   
    
    #print (clf.feature_importances_)
    predictions = clf.predict(testX)
    #print ("number of predictions " + str(len(predictions)))
    pos = 0
    neg = 0
    posneg = 0
    
    for i in range(0, len(testy)):
        if predictions[i] == testy[i]:
           pos += 1 
        elif predictions[i] == 1 and testy[i] == 0:
            posneg += 1
        else:
            neg += 1
    
    elapsed = timeit.default_timer() - start_time
    print("Yggdrassil done in " + str(elapsed) + " seconds")
    
    print (" ------------------results--------------------")
    print ("negetives "+ str(neg))
    
    print ("positive negatives "+ str(posneg))
    
    print ("positives "+ str(pos))
    
    print ("correctness ratio " +  str(pos / len(testy)))

#print(int_generator("637fgb0e587e46c79448da3a2fea83fe") % 1000)

#ins = "stor fed bold"

#hh = hashing_vectorizer(ins.split(' '), 50)
#print(hh)
X, h_X, y = bag_the_words()


randomtree(X.toarray(),y)

randomtree(h_X,y)


#randomtree(wb_X, y)



