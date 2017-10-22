# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from pymongo import MongoClient as Mongo

client = Mongo('localhost',27017)

db = client['Northwind']

import pprint

# Exercise 1
#db.orders.aggregate([
logFile=open('mylogfile'+'.txt', 'w')
#pprint.pprint(list(db.orders.aggregate([
db.orders.aggregate([
        {'$lookup': {
        'from': 'order-details', 
        'localField': 'OrderID', 
        'foreignField': 'OrderID', 
        'as': 'order_details'
            }},
        {'$lookup': {'from' : 'products',
             'localField': "order_details.ProductID",
             'foreignField':'ProductID',
             'as': 'product_details'
         }},
        {'$unwind': '$order_details'},
        # define some conditions here 
        {'$match' : { 'CustomerID' : 'ALFKI' }},
        #define which fields are you want to fetch
        {'$project':{
            'CustomerID': 1,
            'OrderID': 1,
            'order_details' : '$order_details',
            'product_details' : '$product_details'
        }},
        {'$group' : {
            '_id' : {'OrderID' : "$OrderID"},
            'details': { '$push': '$$ROOT'},
            'count' : { '$sum' : 1 }}}
    ])
#), logFile)

logFile.close()

# Exercise 2
logFile=open('Exercise_2'+'.txt', 'w')
pprint.pprint(list(db.orders.aggregate([
#db.orders.aggregate([
        {'$lookup': {
        'from': 'order-details', 
        'localField': 'OrderID', 
        'foreignField': 'OrderID', 
        'as': 'order_details'
            }},
        {'$lookup': {'from' : 'products',
             'localField': "order_details.ProductID",
             'foreignField':'ProductID',
             'as': 'product_details'
         }},
        {'$unwind': '$order_details'},
        # define some conditions here 
        {'$match' : { 'CustomerID' : 'ALFKI' }},
        #define which fields are you want to fetch
        {'$project':{
            'CustomerID': 1,
            'OrderID': 1,
            'order_details' : '$order_details',
            'product_details' : '$product_details' ,
            'size_of_products': {'$size': "$product_details"}

        }},
        {'$match': {"size_of_products": {'$gt': 1}}},
        {'$group' : {
            '_id' : {'OrderID' : "$OrderID"},
            'details': { '$push': '$$ROOT'},
            'count' : { '$sum' : 1 }
            }}
        
    ])
), logFile)            

# Exercise 3
    