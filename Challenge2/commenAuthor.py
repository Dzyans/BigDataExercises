# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 13:02:55 2017

@author: tadah
"""
import sqlite3

from mrjob.job import MRJob
import timeit

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
   

#def get_common_subr(sbr_id):
 #   con = sqlite3.connect('reddit.db')
#    con.text_factory = str ## this is done to decode the shit strings in the database
#    con.isolation_level = None
#    cur = con.cursor()
#    statement = "select subreddit_id from comments where author_id in(select author_id from comments where subreddit_id = '"+ sbr_id +"');"
 
#    if sqlite3.complete_statement(statement):
#        print (statement)
 #       try:
#            statement = statement.strip()
 #           cur.execute(statement)
            
            
            ##if it was a select statement, wil will now iterate the result
#            if statement.lstrip().upper().startswith("SELECT"):
                #sbr_ids = []
                ##sbr_ids = cur.fetchall()
                #print(str(len(sbr_ids )) + " subreddit ids returned")
#                if len(cur) > 1:
#                    for row in cur:##with the id, we get the comments for that subreddit                       
#                        _id = row[0]                 
#                        input_string = str(sbr_id) + " " + str(_id) +"\n"
#                        writeToFile(input_string, "edgy.txt")
                        #get_destinct_author(_id)
#         except sqlite3.Error as e:
#            print ("An error occurred:", e.args[0])
            
#    con.close()
#    print ("done executing")
    
def do():
    con = sqlite3.connect('reddit.db')
    con.text_factory = str ## this is done to decode the shit strings in the database
    con.isolation_level = None
    cur = con.cursor()
    statement = "select id from subreddits limit 2;"
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
                    
                   # get_common_subr(_id)
                    #get_destinct_author(_id)
                    
                
                    
        except sqlite3.Error as e:
            print ("An error occurred:", e.args[0])
            
    con.close()
    return sub_reds_vocab

def writeToFile(string, filepath):
    #print "writing " + str(len(the_list)) + " to " + filepath
    start_time = timeit.default_timer()
    with open(filepath, "a") as file_handler:
        file_handler.write(string)
    elapsed = timeit.default_timer() - start_time
    print ("wrting to file done in: " + str(elapsed))

def get_the_list(limit = "_all"):
    con = sqlite3.connect('reddit.db')
    con.text_factory = str ## this is done to decode the shit strings in the database
    con.isolation_level = None
    cur = con.cursor()
    statement = "select id from authors;"
    edges = 0
    string = ""
    write_count = 0
    if sqlite3.complete_statement(statement):
        start_time = timeit.default_timer()
        #print(statement)
        try:
            statement = statement.strip()
            cur.execute(statement)
            ##if it was a select statement, wil will now iterate the result
            if statement.lstrip().upper().startswith("SELECT"):
                print (str(cur.rowcount) + " authors collected")
                count = 0
                for row in cur:##with the id, we get the comments for that subreddit                       
                    #print(row[0])
                    _id = row[0]
                    #print(count, flush = True)
                    numEdges, input_str = get_subr_for_author(str(_id), limit)
                    
                    edges = edges + numEdges
                    if(numEdges > 0):
                        count = count + 1
                        string = string + input_str
                    
                    if count > 0 and count%10000 == 0:
                        write_count = write_count + 1
                        print("writing to file, write nr. " + str(write_count))
                        elapsed = timeit.default_timer() - start_time
                        print ("running time: " + str(elapsed))
                        writeToFile(string, "common"+limit+".txt")
                        ## reset the string nholder
                        string = ""
                ##write the last bit to the file
                print("wrting the last " + str(count) + " lines")
                writeToFile(string, "common"+limit+".txt")        
        except sqlite3.Error as e:
            print ("An error occurred:", e.args[0])
            
    con.close()
    elapsed = timeit.default_timer() - start_time
    print ("running time: " + str(elapsed))
    print (str(count) + "  lines written")
    print (str(edges) + " edges found")
    print ("done executing")
    

    #select count(distinct subreddit_id) from comments where author_id in(select author_id from comments where subreddit_id = 't5_247i');
def get_subr_for_author(author_id, limit = "_all"):
    con = sqlite3.connect('reddit.db')
    con.text_factory = str ## this is done to decode the shit strings in the database
    con.isolation_level = None
    cur = con.cursor()
    statement = "select distinct subreddit_id from comments where author_id = "+ author_id +" ; "
 
    if sqlite3.complete_statement(statement):
        #print (statement)
        try:
            statement = statement.strip()
            cur.execute(statement)
            
            
            ##if it was a select statement, wil will now iterate the result
            if statement.lstrip().upper().startswith("SELECT"):
                #sbr_ids = []
                ##sbr_ids = cur.fetchall()
                #print(str(len(sbr_ids )) + " subreddit ids returned")
                input_string = ""
                rowCount = 0
                for row in cur:##with the id, we get the comments for that subreddit                       
                    _id = row[0]                 
                    input_string = str(_id) + " " + input_string
                    rowCount = rowCount +1                    
        except sqlite3.Error as e:
            print ("An error occurred:", e.args[0])
            
    con.close()
    #print ("done executing")
    if(rowCount > 1):
        return (((rowCount * (rowCount + 1)) / 2) - rowCount), (input_string+"\n")
    else:
        return 0, ""

def test(rowCount):
    return ((rowCount * (rowCount + 1)) / 2) - rowCount


#print(test(6))

get_the_list()
#Select OrderID, Count(OrderID) as oc from 'Order Details' where OrderID in (Select OrderID from Orders where CustomerID = 'ALFKI') group by OrderID) where oc > 1
##get_subr_for_authors("10")
#do()
#get_common_subr("t5_21n6")             
#do()