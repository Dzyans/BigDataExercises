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
                    #print result
                    #print line
                    #print line.replace("thor", "---------------------------------------------------------------------")
                    #raw_input("Press Enter to continue...")

                    #if pattern in line:
                 #   print "true"
                  #  print line.
                   # raw_input("Press Enter to continue...")
    print counter
lookup("thor")