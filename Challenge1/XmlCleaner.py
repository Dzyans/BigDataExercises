from lxml import etree as et
from bz2file import BZ2File
import os


lookup_dict = {}


def cleanText(text):
    return (text.replace('\n', ' ')).strip(',.').lower()

def parse_xml(parser):
    print "starting parsing" 
    string_list = []
    for events, elem in parser:
        string_list.append(cleanText(elem.text))
    elem.clear()
    writeToFile(string_list, )
    while elem.getprevious() is not None:
        del elem.getparent()[0]        
    
    
def clean_xml(path):
    if path.endswith('.bz2'):
        print 'using bz2 file'
        with BZ2File(path) as xml_file:
            parser = et.iterparse(xml_file, events=('end',),tag=("text","title"))
            parse_xml(parser)
    elif path.endswith('.xml'):
        print 'using xml file'
        parser = et.iterparse(path, events=('end',),tag=("text","title"))
        parse_xml(parser)
    else:
        directory = os.path.join(os.getcwd(),path)
        for root,dirs,files in os.walk(directory):
            for file in files:
                print file
                with BZ2File('chunks\\'+file) as xml_file:
                    parser = et.iterparse(xml_file, events=('end',),tag=("text","title"))
                    parse_xml(parser)

def writeToFile(the_list, filepath):
    print "writing " + str(len(the_list)) + " to " + filepath
    with open(filepath, "w+") as file_handler:
        for item in the_list:
            file_handler.write(item.encode('utf8'))

def update_dict(the_dict, list_of_words, filename_nr):
    cock_block_set = set()
    ##set up the set of unique words
    for line in list_of_words:
        words = line.split(' ')
        for word in words:
            cock_block_set.add(word)
    ##add them to dict
    for word in cock_block_set:
        if word in the_dict:
            if word == ' ':
                break  ##ignore lefter over blank sapaces
                ##increment word count
            #print "adding "+ word + " to dict"
            the_dict[word].append(filename_nr)
            #fileList.append(filename_nr)
            #the_dict[word] = fileList
        else:
            fileList = list() ##key does not exist, so insert list at as value
            fileList.append(filename_nr)
            the_dict[word] = fileList

    print str(len(cock_block_set)) + " words in set"
    return the_dict
        
path = "chunks"
#path = "duncan.xml"

print path
cleaned = clean_xml(path)
    
            