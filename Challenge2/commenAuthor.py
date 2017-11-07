# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 13:02:55 2017

@author: tadah
"""
import sqlite3
from collections import OrderedDict
from operator import itemgetter

def do():
    con = sqlite3.connect('reddit.db')
    con.text_factory = str ## this is done to decode the shit strings in the database
    con.isolation_level = None
    cur = con.cursor()
    statement = "select id from subreddits limit 50;"
    # d = OrderedDict(sorted(data.items(), key=itemgetter(1)))
    ##counters
 
    sub_reds_vocab = OrderedDict()
    
    if sqlite3.complete_statement(statement):
        print (statement)
        try:
            statement = statement.strip()
            cur.execute(statement)
            print ("done executing")
            
            ##if it was a select statement, wil will now iterate the result
            if statement.lstrip().upper().startswith("SELECT"):
                sbr_ids = []
                sbr_ids = cur.fetchall()
                print(str(len(sbr_ids )) + " subreddit ids returned")
                for sbr_id in sbr_ids:##with the id, we get the comments for that subreddit                       
                    _id = sbr_id[0]                    
                    
                    get_destinct_author(_id)
                    
                
                    
        except sqlite3.Error as e:
            print ("An error occurred:", e.args[0])
            
    con.close()
    return sub_reds_vocab

def writeToFile(string, filepath):
    #print "writing " + str(len(the_list)) + " to " + filepath
    with open(filepath, "a") as file_handler:
        file_handler.write(string)
    

def get_destinct_author(sbr_id, verbose = False):
    print (sbr_id + ": ")
    con = sqlite3.connect('reddit.db')
    con.text_factory = str ## this is done to decode the shit strings in the database
    con.isolation_level = None
    cur = con.cursor()
    statement = "select distinct author_id from comments where subreddit_id = '" + sbr_id + "';"
    
    #print (statement)
    if sqlite3.complete_statement(statement):
        #print (statement)
        try:
            statement = statement.strip()
            cur.execute(statement)
            vocab = set()
            commentCount = 0
            for row in cur:
                #print ("parsing next comment")
                #print (row[0] + ", " + sbr_id)
                writeToFile(sbr_id + " " + row[0]+"\n", "data.txt")
               
                #print ("words added to set")
            
          
           
            return vocab, commentCount
        except sqlite3.Error as e:
            print ("An error occurred:", e.args[0])
                
do()