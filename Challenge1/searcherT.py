import xml.etree as ET
import os
import re

def lookup(pattern):
    counter = 0
    for filename in os.listdir("A"):
        print filename
        with open("A/"+filename, 'r') as searchfile:
            for line in searchfile:
                result = re.findall('\\b'+pattern+'\\b', line, flags=re.IGNORECASE)
                if len(result) > 0:
                    counter = counter +1

    print counter
lookup("thor")