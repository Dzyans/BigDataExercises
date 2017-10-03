
import xml.etree.ElementTree as etree
def parseAndWrite():
    counter = 0
    with open("/home/dzyan/Dokumenter/enwiki-20170820-pages-articles-multistream.xml") as xml:
        for event, elem in etree.iterparse(xml, events=('start', 'end', 'start-ns', 'end-ns')):
            if event == "end" and elem.tag == "{http://www.mediawiki.org/xml/export-0.10/}page":
                for a in elem:
                    if a.tag == "{http://www.mediawiki.org/xml/export-0.10/}revision":
                        for b in a:
                            if b.tag == "{http://www.mediawiki.org/xml/export-0.10/}text":
                                print b.text
        elem.clear()

                ##print "found"
    print counter


def anohterParser():
    with open("/home/dzyan/Dokumenter/enwiki-20170820-pages-articles-multistream.xml") as xml:

        # get an iterable
        context = etree.iterparse(xml, events=("start", "end"))

        # turn it into an iterator
        context = iter(context)

        # get the root element
        event, root = context.next()

        for event, elem in context:
            if event == "end" and elem.tag == "{http://www.mediawiki.org/xml/export-0.10/}page":



                root.clear()
def pp():
    import xml.etree.ElementTree as ET
    tree = ET.parse('/home/dzyan/Dokumenter/enwiki-20170820-pages-articles-multistream.xml')



#pp()
parseAndWrite()
#anohterParser()