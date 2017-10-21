# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from pymongo import MongoClient as Mongo

client = Mongo('localhost',27017)

db = client['Northwind']
print client.database_names()


print db.collection_names()

orders  = db.orders
order_details = db["order-details"]
products = db.products
customers = db.customers

#print customers.find_one({"CustomerID ": "ALFKI"})

#print orders.find_one({ "CustomerID" : 'ALFKI' })



#Exercise 1

for order in orders.find({ "CustomerID" : "ALFKI" }):
 #   #print order["OrderID"]
    for detail in order_details.find({"OrderID" : order["OrderID"]}):
   #     print detail["ProductID"]
        for product in products.find({"ProductID" : detail["ProductID"]}):
            print product["ProductName"]


# Exercise 2
            

