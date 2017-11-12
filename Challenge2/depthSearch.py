# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 16:11:15 2017

@author: tadah
"""

import sqlite3

def get_id_parent_id_pair(sbr_id):
    con = sqlite3.connect('reddit.db')
    con.text_factory = str ## this is done to decode the shit strings in the database
    con.isolation_level = None
    cur = con.cursor()
    statement = "select id, parent_id from comments where subreddit_id = '"+ sbr_id +"';"
 
    if sqlite3.complete_statement(statement):
        print (statement)
        try:
            statement = statement.strip()
            cur.execute(statement)
            
            
            ##if it was a select statement, wil will now iterate the result
            if statement.lstrip().upper().startswith("SELECT"):
                #sbr_ids = []
                ##sbr_ids = cur.fetchall()
                #print(str(len(sbr_ids )) + " subreddit ids returned")
                for row in cur:##with the id, we get the comments for that subreddit                       
                    _id = row[0]
                    _pid = row[1]
                    input_string = str(_pid) + " " + str(_id) +"\n"
                    writeToFile(input_string, "id_pid2.txt")
                    #get_destinct_author(_id)
                    
                
                    
        except sqlite3.Error as e:
            print ("An error occurred:", e.args[0])
            
    con.close()
    print ("done executing")

def do():
    con = sqlite3.connect('reddit.db')
    con.text_factory = str ## this is done to decode the shit strings in the database
    con.isolation_level = None
    cur = con.cursor()
    statement = "select id from subreddits limit 5;"
    # d = OrderedDict(sorted(data.items(), key=itemgetter(1)))
    ##counters
 
    sub_reds_vocab = []
    
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
                    sub_reds_vocab.append(_id)
                   # get_common_subr(_id)
                    #get_destinct_author(_id)
                    
                
                    
        except sqlite3.Error as e:
            print ("An error occurred:", e.args[0])
            
    con.close()
    return sub_reds_vocab
    
    
def writeToFile(string, filepath):
    #print "writing " + str(len(the_list)) + " to " + filepath
    with open(filepath, "a") as file_handler:
        file_handler.write(string)
for ele in do():
    get_id_parent_id_pair(ele)
    