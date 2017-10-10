import re
import os
import time
import numpy as np
def lookup(pattern, lookup_list):
    hit = 0
    #print len(lookup_list)
    counter = 0
    for filename in os.listdir("A"):
        filenum = int(filename[4:])

        #print filenum
        if(filenum) in lookup_list:
            #print filename
            with open("A/"+filename, 'r') as searchfile:
                for line in searchfile:
                    result = match(pattern, line)
                    if len(result) > 0:
                        hit = hit +1
                        print result
    print hit
def simple_lookup(pattern):
    print "doing simple"
    counter = 0
    file_counter = 0
    for filename in os.listdir("A"):
       file_counter = file_counter +1
       with open("A/"+filename, 'r') as searchfile:
            for line in searchfile:
                result = match(pattern, line)
                if len(result) > 0:
                    print filename
                    print result
                    print str(file_counter) + " searched so far"
                    counter = counter+1
    print "done " + str(counter)
def match(query, test_data):
    x = ''
    for element in query:
        if type (element) is str:
            y = element
        elif type(element) is list:
            y = '.{%s,%s}'%(str(element[0]),str(element[1]))
        x = '%s%s'%(x,y)
    #print x
    pattern = re.compile(x)
    return pattern.findall(test_data)

def printout_dict(words):
    dict_list = list()
    for filename in os.listdir("Meta"):
        #print filename
        dict_list.append(np.load('Meta/'+filename).item())
        ##dict_list.add(np.load('Meta/my_file1.npy').item())
    print "done loading dict"
    print len(dict_list)
    list_of_lists = []

    for MetaDict in dict_list:
        for key in words:
            if key in MetaDict:
                list_of_lists.append(MetaDict[key])

    print list_of_lists
    if len(list_of_lists) == 1:
        return list_of_lists

    curset = set(list_of_lists[0])

    for d in list_of_lists:
        curset = set(d).intersection(curset)

    print "hej"
    print curset
    #for k, v in read_dictionary.items():
     #   print(k, v)
def load_dicts():
    dict_list = list()
    for filename in os.listdir("MetaA"):
        # print filename
        new_dict = np.load('MetaA/' + filename).item()
        print "loaded dict " + filename
        print len(new_dict)
        dict_list.append(new_dict)

    return dict_list

def GetList(words):
    #print len(dict_list)
    cur_list_of_list = []
    ll = []
    curList = []
    for filename in os.listdir("MetaA"):
        print "NEXT"
        MetaDict = np.load('MetaA/' + filename).item()

        #print "next dict"
        #curList = list()
        ll = []
        for key in words:
            if key in MetaDict:
                ll.append(MetaDict[key])
        if(len(ll) > 0):
            curList = set(ll[0])
            for hej in range(1, len(ll)):
                curList = set(curList).intersection(set(ll[hej]))
        #   print "common values found"
        #   print curList
            cur_list_of_list = cur_list_of_list + list(curList)
            curList = []

    return cur_list_of_list


#test = "i have a really nice cat in hat at home"
#pattern = ["cat", [2,4], "hat"]
#pattern = ["when", [15,25],"republic",[15,25],"along"]

#pattern = ["cats",[0,10], "are", [0,10], "to"]
#pattern = ["or",[0,10], "or", [0,10], "or"]
pattern = ["when",[15,25], "republic", [15,25], "along"]

#start_time = time.time()
#dicts = load_dicts()
#print("---dicts loaded in %s seconds ---" % (time.time() - start_time))


#hh = GetList(["or"])
#hh = GetList(["cats","are","to"])
hh = GetList(["when","republic","along"])
start_time = time.time()
lookup(pattern, hh)

print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()

simple_lookup(pattern)

print("--- %s seconds ---" % (time.time() - start_time))
#print (printout_dict())
#print match(pattern, test)
#lookup(pattern)#
#if len(list_of_lists) == 1:
#    cur_list_of_list.append(list_of_lists)
#else:

#curset = set(list_of_lists[0])

#for d in list_of_lists:
#
#cur_list_of_list.append(curset)
