import re
import os
import numpy as np
def lookup(pattern):

    counter = 0
    for filename in os.listdir("B"):
        #print filename
        with open("B/"+filename, 'r') as searchfile:
            for line in searchfile:
                result = match(pattern, line)
                if len(result) > 0:
                    print result

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
    for filename in os.listdir("Meta"):
        # print filename
        dict_list.append(np.load('Meta/' + filename).item())

    return dict_list

def GetList(words, dict_list):

            ##dict_list.add(np.load('Meta/my_file1.npy').item())
        print "done loading dict"
        print len(dict_list)
        cur_list_of_list = []
        ll = []
        curList = []
        for MetaDict in dict_list:
            print "next dict"
            for key in words:
                if key in MetaDict:
                    print "word found in "
                    print MetaDict[key]
                    ll.append(MetaDict[key])
            curList = set(ll[0])
            for hej in range(1, len(ll)):
                curList = set(curList).intersection(set(ll[hej]))

            cur_list_of_list.append(list(curList))
            curList = []

        print "hej"
        print len(cur_list_of_list)
        print(cur_list_of_list)


#test = "i have a really nice cat in hat at home"
#pattern = ["cat", [2,4], "hat"]
#pattern = ["when", [15,25],"republic",[15,25],"along"]

pattern = ["when", [15,25],"republic"]
dicts = load_dicts()

GetList(["republic","rhodesia"], dicts)

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
