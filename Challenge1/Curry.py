import re
import os

def lookup(pattern):
    counter = 0
    for filename in os.listdir("A"):
        #print filename
        with open("A/"+filename, 'r') as searchfile:
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
    
#test = "i have a really nice cat in hat at home"
#pattern = ["cat", [2,4], "hat"]
pattern = ["when", [15,25],"republic",[15,25],"along"]

#print match(pattern, test)
lookup(pattern)
