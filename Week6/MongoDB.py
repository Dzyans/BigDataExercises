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
logFile=open('Exercise1'+'.txt', 'w')
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
), logFile)

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
        #{'$match': {"order_details":{'$ne':[]}}},
        {'$lookup': {'from' : 'products',
             'localField': "order_details.ProductID",
             'foreignField':'ProductID',
             'as': 'product_details'
         }},
        #{'$match': {"product_details":{'$ne':[]}}},

        # define some conditions here 
        {'$match' : { 'CustomerID' : 'ALFKI' }},
        #define which fields are you want to fetch
        {'$project':{
            'size_of_products': {'$size': "$product_details"},
            'CustomerID': 1,
            'OrderID': 1,
            'order_details' : '$order_details',
            'product_details' : '$product_details' 
        }},
        {'$match': {"size_of_products": {'$gt': 1}}},
        {'$group' : {
            '_id' : {'OrderID' : "$OrderID"},
            'details': { '$push': '$$ROOT'},
            }}
        
    ])
), logFile)            
logFile.close()

logFile=open('Exercise_3'+'.txt', 'w')

# Exercise 3
pprint.pprint(list(db.products.aggregate([
    {'$lookup': {
        'from': 'order-details', 
        'localField': 'ProductID', 
        'foreignField': 'ProductID', 
        'as': 'order_details'
    }},
    {'$unwind': '$order_details'},
    {'$match': {"order_details":{'$ne':[]}}},
    
    {'$lookup': {
        'from': 'orders', 
        'localField': 'order_details.OrderID', 
        'foreignField': 'OrderID', 
        'as': 'orders'
    }},
    {'$unwind': '$orders'},
    {'$match': {"orders":{'$ne':[]}}},
    {'$match' : { 'orders.CustomerID' : 'ALFKI' }},

        {'$project':{
        'ProductID': 1,
        'ProductName': 1,
        'CustomerID': '$orders.CustomerID',
        'orders' : '$orders',
        'total' : {'$sum' : '$order_details.Quantity'},
        }},
        {'$group' : {
            '_id' : {'ProductID' : "$ProductID"},
            'details': { '$push': '$$ROOT'},
            }}
])
), logFile)            
logFile.close()
