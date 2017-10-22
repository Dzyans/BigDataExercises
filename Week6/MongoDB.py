# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from pymongo import MongoClient as Mongo

client = Mongo('localhost',27017)

db = client['Northwind']

import pprint

#pprint.pprint(list(db.orders.aggregate([
#        {'$match' : { 'CustomerID' : 'ALFKI' }}])
#))

pprint.pprint(list(db.orders.aggregate([
        {'$lookup': {
        'from': 'order-details', 
        'localField': 'OrderID', 
        'foreignField': 'OrderID', 
        'as': 'order_details'
            }
        },
        {'$unwind': '$order_details'},
        {'$lookup': {'from' : 'products',
                     'localField': "ProductID",
                     'foreignField': 'order_details.ProductID',
                     'as': 'product_details'
         }},
        {'$unwind': '$product_details'},
        {'$match' : { 'CustomerID' : 'ALFKI' }}      
    ])
))

#Exercise 1
orders  = db.orders
#order_details = db["order-details"]
#products = db.products
#customers = db.customers


#for order in orders.find({ "CustomerID" : "ALFKI" }):
#    print order.order_details
#    for detail in order_details.find({"OrderID" : order["OrderID"]}):
#        print detail["ProductID"]
#        for product in products.find({"ProductID" : detail["ProductID"]}):
#            product["ProductName"]


# Exercise 2
            
#for order in orders.find({ "CustomerID" : "ALFKI" }):
    #print order["OrderID"]
 #   for detail in order_details.find({"OrderID" : order["OrderID"]}):
#        detail