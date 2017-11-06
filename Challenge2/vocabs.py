# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 23:39:26 2017

@author: tadah
"""

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

def get_stuff(statement, verbose = False):
    con = sqlite3.connect('reddit.db')
    con.text_factory = str ## this is done to decode the shit strings in the database
    con.isolation_level = None
    cur = con.cursor()
    
    if sqlite3.complete_statement(statement):
            print (statement)
            try:
                statement = statement.strip()
                cur.execute(statement)
                print ("done executing")
                
                ##if it was a select statement, wil will now iterate the result
                if statement.lstrip().upper().startswith("SELECT"):
                    values = cur.fetchone()
                    print(str(len(values)) + " entries returned")
                    if(verbose and len(values) > 0):
                        names = list(map(lambda x: x[0], cur.description))
                        print (names)
                        for val in values:
                            print (val[0])
                    
                 
            except sqlite3.Error as e:
                print ("An error occurred:", e.args[0])
            
    con.close()

def add_words_to_set(the_set, the_string):
    symbols = ['\n','`','~','!','@','#','$','%','^','&','*','(',')','_','-','+','=','{','[',']','}','|','\\',':',';','"',"'",'<','>','.','?','/',',']
    
    #s = """**Most Popular Comments**   \n\n---\n|Score|Author|Post Title|Link to comment|\n|:-|-|-|-|\n|4186|/u/DrowningDream|[WP] A Man gets to paradise. Unfortunately, Lucifer won the War"""
    
    the_string = the_string.lower()
    for sym in symbols:
    	the_string = the_string.replace(sym, " ")
    
    for w in the_string.split(" "):
    	if len(w.replace(" ","")) > 0:
    		the_set.add(w)

def get_vocabularySet(sbr_id):
    con = sqlite3.connect('reddit.db')
    con.text_factory = str ## this is done to decode the shit strings in the database
    con.isolation_level = None
    cur = con.cursor()
    statement = "select body from comments where subreddit_id = '" + sbr_id + "';"
    #print (statement)
    if sqlite3.complete_statement(statement):
        #print (statement)
        try:
            statement = statement.strip()
            cur.execute(statement)
            vocab = set()
            for row in cur:
                ##print (row[0])
                add_words_to_set(vocab, row[0])
            return vocab
        except sqlite3.Error as e:
            print ("An error occurred:", e.args[0])
                


def get_vocabs():
    con = sqlite3.connect('reddit.db')
    con.text_factory = str ## this is done to decode the shit strings in the database
    con.isolation_level = None
    cur = con.cursor()
    statement = "select id from subreddits;"
    
    best_id = []
    
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
                    vocabulary = get_vocabularySet(sbr_id[0])
                    print (len(vocabulary))
        except sqlite3.Error as e:
            print ("An error occurred:", e.args[0])
            
    con.close()

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
                    values = cur.fetchall()
                    names = list(map(lambda x: x[0], cur.description))
                    print (names)
                    for val in values:
                        print (val)
            except sqlite3.Error as e:
                print ("An error occurred:", e.args[0])
            buffer = ""

    con.close()
    
GO()
#get_stuff("select * from comments;")
#get_vocab()
get_vocabs()
#get_vocabs("select * from comments where subreddit_id = 't5_2r0gj' limit 3;", True)
#db_shell()