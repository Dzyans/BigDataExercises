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

def printout_dict():
    read_dictionary = np.load('my_file.npy').item()
    for k, v in read_dictionary.items():
        print(k, v)


#test = "i have a really nice cat in hat at home"
#pattern = ["cat", [2,4], "hat"]
pattern = ["when", [15,25],"republic",[15,25],"along"]

printout_dict()
#print match(pattern, test)
#lookup(pattern)
