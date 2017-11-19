# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 16:11:15 2017

@author: tadah
"""

import sqlite3
import timeit

def get_id_parent_id_pairs(sbr_id):
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
            edge_counter = 0
            
            ##if it was a select statement, wil will now iterate the result
            if statement.lstrip().upper().startswith("SELECT"):
                input_string = ""
                for row in cur:##with the id, we get the comments for that subreddit                       
                    edge_counter = edge_counter + 1
                    _id = row[0]
                    _pid = row[1]
                    input_string = input_string + str(_pid) + " " + str(_id) +"\n"
                return edge_counter, input_string
                    
        except sqlite3.Error as e:
            print ("An error occurred:", e.args[0])
            
    con.close()

def do():
    con = sqlite3.connect('reddit.db')
    con.text_factory = str ## this is done to decode the shit strings in the database
    con.isolation_level = None
    cur = con.cursor()
    statement = "select id from subreddits;"
    # d = OrderedDict(sorted(data.items(), key=itemgetter(1)))
    ##counters
   
    if sqlite3.complete_statement(statement):
        print (statement)
        try:
            statement = statement.strip()
            cur.execute(statement)
            print ("done executing")
            
            ##if it was a select statement, wil will now iterate the result
            if statement.lstrip().upper().startswith("SELECT"):
                sbr_ids = []
                
                print(str(len(sbr_ids )) + " subreddit ids returned")
                count = 0
                string = ""
                edges = 0
                write_count = 1
                for sbr_id in cur:                       
                    _id = sbr_id[0]                    
                    numEdges, input_str = get_id_parent_id_pairs(_id)
                
                    edges = edges + numEdges
                    if(numEdges > 0):
                        count = count + 1
                        string = string + input_str
                
                    if edges > 100000*write_count:
                            write_count = write_count + 1
                            print("writing to file, write nr. " + str(write_count))
                            #elapsed = timeit.default_timer() - start_time
                            #print ("running time: " + str(elapsed))
                            writeToFile(string, "pid_id2.txt")
                            ## reset the string nholder
                            string = ""
                    print(edges)
                print("wrting the last " + str(edges) + " lines")
                writeToFile(string, "pid_id4.txt")  
        except sqlite3.Error as e:
            print ("An error occurred:", e.args[0])
            
    con.close()
    

def do_it():
    con = sqlite3.connect('reddit.db')
    con.text_factory = str ## this is done to decode the shit strings in the database
    con.isolation_level = None
    cur = con.cursor()
    statement =  "select subreddit_id, parent_id, id from comments where subreddit_id in ('t5_2qh1i','t5_2qh33','t5_2qh0u','t5_2qh13', 't5_2qqjc','t5_30uy0','t5_2qh1e','t5_2rfxx','t5_2sgp1','t5_2s7tt');"
    # d = OrderedDict(sorted(data.items(), key=itemgetter(1)))
    ##counters
    print(statement)
    if sqlite3.complete_statement(statement):
        print ("is good")
        try:
            print ("trying")
            statement = statement.strip()
            cur.execute(statement)
            print ("done executing")
            
            ##if it was a select statement, wil will now iterate the result
            if statement.lstrip().upper().startswith("SELECT"):
                count = 0
                metacount = 0
                input_string = ""
                write_count = 1
                
                for row in cur:
                                          
                    count = count + 1
                    metacount = metacount +1
                    _sbr_id = row[0]
                    _id = row[2]
                    _pid = row[1]
                    input_string = input_string + str(_sbr_id) + " " + str(_pid) + " " + str(_id) +"\n"
                
                        
                    if count > 0 and count%100000 == 0:
                            write_count = write_count + 1
                            print("writing to file, write nr. " + str(write_count))
                            #elapsed = timeit.default_timer() - start_time
                            #print ("running time: " + str(elapsed))
                            writeToFile(input_string, "sbr_id_pid_id_subset2.txt")
                            ## reset the string nholder
                            input_string = ""
                            count = 0
                    
                print("wrting the last " + str(count) + " lines")
                writeToFile(input_string, "sbr_id_pid_id_subset2.txt") 
                print(str(metacount) + " written in total")
        except sqlite3.Error as e:
            print ("An error occurred:", e.args[0])
            
    con.close()
    
def writeToFile(string, filepath):
    #print "writing " + str(len(the_list)) + " to " + filepath
    #start_time = timeit.default_timer()
    with open(filepath, "a") as file_handler:
        file_handler.write(string)
    #elapsed = timeit.default_timer() - start_time
    #print ("wrting to file done in: " + str(elapsed))

start_time = timeit.default_timer()
do_it()
elapsed = timeit.default_timer() - start_time
print ("All data written in: " + str(elapsed) + " seconds")
