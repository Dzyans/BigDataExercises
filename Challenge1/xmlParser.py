
import xml.etree.ElementTree as etree
def parseAndWrite(path, id_tag):
    counter = 0
    metaCounter = 0
    string_list = []
    ##"{http://www.mediawiki.org/xml/export-0.10/}"
    #with open("/home/dzyan/Dokumenter/enwiki-20170820-pages-articles-multistream.xml") as xml:
    with open(path) as xml:
        for event, elem in etree.iterparse(xml, events=('start', 'end', 'start-ns', 'end-ns')):
            if event == "end" and elem.tag == id_tag+"page":
                proceed = False
                for a in elem:
                    if a.tag == id_tag+"title":
                        #print a.text
                        if a.text[0] == "A" or a.text[0] == "a":
                            proceed = True
                            counter = counter +1
                            metaCounter = metaCounter+1
                            #print counter
                        #if(metaCounter > 1000):
                         #   print "-----------done for now, "+ str(counter) +" files written"
                          #  return string_list
                    if a.tag == id_tag+"revision" and proceed:
                       for b in a:
                          if b.tag == id_tag+"text":
                             string_list.append(cleanText(b.text) + u"\n" + u"\n")
                if len(string_list) == 100:
                    writeToFile(string_list, "A/A"+ str(metaCounter/100))
                    ##reset and go on
                    counter = 0
                    string_list = []
                elem.clear()


def cleanText(text):
    return text.replace('\n', ' ')

def writeToFile(the_list, filepath):
    print "writing " + str(len(the_list)) + " to " + filepath
    with open(filepath, "w+") as file_handler:
        for item in the_list:
            file_handler.write(item.encode('utf8'))


path = "/home/dzyan/Dokumenter/enwiki-20170820-pages-articles-multistream.xml"
tag_id = "{http://www.mediawiki.org/xml/export-0.10/}"
listen = parseAndWrite(path, tag_id)
#print listen
writeToFile(listen, "A")