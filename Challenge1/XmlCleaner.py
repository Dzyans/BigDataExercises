from lxml import etree as et
from bz2file import BZ2File

def cleanText(text):
    return (text.replace('\n', ' ')).strip(',.').lower()

def parse_xml(parser):
    print "starting parsing" 
    for events, elem in parser:
        #print elem.tag        
        print cleanText(elem.text)             
    elem.clear()
    # Also eliminate now-empty references from the root node to node        
    while elem.getprevious() is not None:
        del elem.getparent()[0]        
   
def clean_xml(path):
    if path.endswith('.bz2'):
        print 'using bz2 file'
        with BZ2File(path) as xml_file:
            parser = et.iterparse(xml_file, events=('end',),tag=("text"))
            parse_xml(parser)
    elif path.endswith('.xml'):
        print 'using xml file'
        parser = et.iterparse(path, events=('end',),tag=("text","title"))
        parse_xml(parser)
    else:
        print 'error'
        return
        
path = "chunks/chunk-1.xml.bz2"
#path = "duncan.xml"

print path
cleaned = clean_xml(path)
    
            