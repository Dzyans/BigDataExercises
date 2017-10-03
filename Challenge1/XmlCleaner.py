from lxml import etree as et
import bz2file as BZ2File

def cleanText(text):
    return (text.replace('\n', ' ')).strip(',.').lower()
    
def clean_xml(path):
    #if path.endswith('.bz2'):
    print 'using bz2 file'
    with BZ2File(path) as xml_file:
        parser = et.iterparse(xml_file, events=('end',),tag='text')
    #elif path.endswith('.xml'):
    #    print 'using xml file'
    #    parser = et.iterparse(path, events=('end',),tag="text")
    #else:
    #    print 'error'
    #    return
        for events, elem in parser: 
                print cleanText(elem.text)             
        elem.clear()
    
    # Also eliminate now-empty references from the root node to node        
    while elem.getprevious() is not None:
        del elem.getparent()[0]    
    
path = "/zhome/a5/5/77597/Downloads/enwiki-20170620-pages-articles-multistream.xml.bz2"
#path = "/zhome/a5/5/77597/python/BigDataExercises/Challenge1/duncan.xml"
#path = "/zhome/a5/5/77597/python/BigDataExercises/Challenge1/udklip.xml"

print path
cleaned = clean_xml(path)
    
            