import re 

def match(query, test_data, ):
    x = ''
    for element in query:
        if type (element) is str:
            y = element
        elif type(element) is list:
            y = '.{%s,%s}'%(str(element[0]),str(element[1]))
        x = '%s%s'%(x,y)
    pattern = re.compile(x)        
    return pattern.search(test_data).group(0)
    
test = "i have a really nice cat in hat at home"
pattern = ["cat", [2,4], "hat"]
print match(pattern, test)

