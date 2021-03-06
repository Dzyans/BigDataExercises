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
from collections import OrderedDict
import timeit

def add_words_to_set(the_set, the_string, verbose = False):
    word_count = 0
    symbols = ['\n','`','~','!','@','#','$','%','^','&','*','(',')','_','-','+','=','{','[',']','}','|','\\',':',';','"',"'",'<','>','.','?','/',',']
    
    #s = """**Most Popular Comments**   \n\n---\n|Score|Author|Post Title|Link to comment|\n|:-|-|-|-|\n|4186|/u/DrowningDream|[WP] A Man gets to paradise. Unfortunately, Lucifer won the War"""
    
    the_string = the_string.lower()
    for sym in symbols:
    	the_string = the_string.replace(sym, " ")
    
    for w in the_string.split(" "):
    	if len(w.replace(" ","")) > 0:
            the_set.add(w)
            word_count = word_count + 1
    if verbose:
        print(str(word_count)+ " words iterated")

def get_vocabularySet(sbr_id, verbose = False):
    print (sbr_id + ": ")
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
            commentCount = 0
            for row in cur:
                #print ("parsing next comment")
                ##print (row[0])
                add_words_to_set(vocab, row[0], verbose)
                commentCount = commentCount + 1
                #print ("words added to set")
            
            print ("vocabulary: " + str(len(vocab)))
            print("    " + str(commentCount) + " comments")
           
            return vocab, commentCount
        except sqlite3.Error as e:
            print ("An error occurred:", e.args[0])
                
def get_vocabs():
    con = sqlite3.connect('reddit.db')
    con.text_factory = str ## this is done to decode the shit strings in the database
    con.isolation_level = None
    cur = con.cursor()
    statement = "select id from subreddits;"
    # d = OrderedDict(sorted(data.items(), key=itemgetter(1)))
    ##counters
    total_comments = 0
    comments = 0
    all_comments = 53850000
    
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
                    
                    vocabulary, comments = get_vocabularySet(_id)
                    
                    ##just counting shit
                    total_comments = total_comments + comments
                    print("    " + str(total_comments) + " Total. " + str(all_comments - total_comments) + " comments to go.")
                    sub_reds_vocab[_id] = len(vocabulary)
                    
        except sqlite3.Error as e:
            print ("An error occurred:", e.args[0])
            
    con.close()
    return sub_reds_vocab

def with_sorted(the_dict):
     return sorted(the_dict.items(), key=(lambda x: x[1]), reverse=True)[:10]

start_time = timeit.default_timer()
vocabs = get_vocabs()

svocabs = with_sorted(vocabs)

for k in svocabs:
    print (k)
    
elapsed = timeit.default_timer() - start_time
print ("Counting and sorting done in: " + str(elapsed) + " seconds")

#get_vocabularySet("t5_2qh1i")
#get_vocabs("select * from comments where subreddit_id = 't5_2r0gj' limit 3;", True)

#select subreddit_id from comments where author_id in(select author_id from comments where subreddit_id = 't5_247i');
#select count(distinct subreddit_id) from comments where author_id in(select author_id from comments where subreddit_id = 't5_247i');
