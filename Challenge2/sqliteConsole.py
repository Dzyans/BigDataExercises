# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 22:47:18 2017

@author: tadah
"""

import sqlite3

def GO():
    conn = sqlite3.connect('reddit.db')
    ##copy fuckin paste
    c = conn.cursor()

    # Get all tables
    c.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;")

    print (c.fetchall())

    conn.close()

def db_shell():
    con = sqlite3.connect('reddit.db')
    con.text_factory = str ## this is done to decode the shit strings in the database
    con.isolation_level = None
    cur = con.cursor()

    buffer = ""

    print ("Enter your SQL commands to execute in sqlite3.")
    print ("Enter a blank line to exit.")

    while True:
        line = input()
        if line == "":
            break
        buffer += line
        ##print buffer
        if sqlite3.complete_statement(buffer):
            print (buffer)
            try:
                buffer = buffer.strip()
                cur.execute(buffer)

                if buffer.lstrip().upper().startswith("SELECT"):
                    
                    names = list(map(lambda x: x[0], cur.description))
                    print (names)
                    print (cur.rowcount)
                    counter = 0
                    for row in cur:
                        counter = counter +1
                        print(counter)
                    print (counter)
                        #print (row)
            except sqlite3.Error as e:
                print ("An error occurred:", e.args[0])
            buffer = ""

    con.close()
        #Select OrderID, Count(OrderID) as oc from 'Order Details' where OrderID in (Select OrderID from Orders where CustomerID = 'ALFKI') group by OrderID) where oc > 1

GO()
db_shell()