
import xml.etree.ElementTree as etree
def parseAndWrite(path, id_tag):
    counter = 0
    ##"{http://www.mediawiki.org/xml/export-0.10/}"
    #with open("/home/dzyan/Dokumenter/enwiki-20170820-pages-articles-multistream.xml") as xml:
    with open(path) as xml:
        for event, elem in etree.iterparse(xml, events=('start', 'end', 'start-ns', 'end-ns')):
            if event == "end" and elem.tag == id_tag+"page":
                for a in elem:
                    if a.tag == id_tag+"title":
                        print a.text
                        if a.text[0] != "H" and a.text[0] != "h":
                            print a.text
                            print "-----------------------break-----------------------"
                            return
                    if a.tag == id_tag+"revision":
                        for b in a:
                            if b.tag == id_tag+"text":
                                print cleanText(b.text)
        elem.clear()

                ##print "found"
    print counter


def cleanText(text):
    return text.replace('\n', ' ')

parseAndWrite("")