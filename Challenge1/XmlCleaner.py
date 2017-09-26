import zipfile as zip
import os
import fnmatch as fn
import re
from xml.etree import ElementTree as ET
def iterate_dir(path):
    dir = os.path.abspath("")
    extension = ".zip"
    for item in os.listdir(dir):
        if item.endswith(extension):
            zip_file = zip.ZipFile(item, 'r')
            for name in zip_file.namelist():
                if fn.fnmatch(name, '*.xml'):
                    cleanXmlFiles(zip_file.read(name))
            #print(os.path.join(dir, item))
            #zip_file.extractall(dir+"/out")
            #zip_file.close()

def cleanXmlFiles(name):
    tree = ET.fromstring(name)
    ET.tostring(tree, method='text')
    #match = re.search(r'[0-9A-Z]', name)
    #print match.string
    #clean = re.match(u"[^(\w+)]+",u" ",name)
    #print clean

    #tree = etree.parse(name)

    #notags = etree.tostring(tree, encoding="utf8", method="text")
    #print notags
    #xmlx.elemdict(name.)
    #for line in name.:
     #   print line
        ##print re.match("(\w+)", line)


iterate_dir("jek")