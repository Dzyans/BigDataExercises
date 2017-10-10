import numpy as np
import xml.etree.ElementTree as etree
import lxml.etree as letree
def parseAndWrite(path, id_tag, files_size):
    lookup_dict = {}
    counter = 0
    metaCounter = 0
    total = 0
    string_list = []

    ##"{http://www.mediawiki.org/xml/export-0.10/}"
    #with open("/home/dzyan/Dokumenter/enwiki-20170820-pages-articles-multistream.xml") as xml:
    proceed = False
    skipcounter = 0
    current_title = "A"
    with open(path) as xml:
        for event, elem in letree.iterparse(xml, events=('start', 'end')):
            if event == "end" and elem.tag == id_tag+"page":
                total = total +1
                proceed = True
                justsaved = False
                for a in elem:
                    if a.tag == id_tag+"title":
                        if a.text == 'Cat' or a.text[0] == 'a':
                            text = cleanText(b.text)
                            string_list.append(text)
                            writeToFile(string_list, "B/part" + str(metaCounter / files_size))
                         #   proceed = True
                        #else:
                         #   skipcounter = skipcounter +1
                        the_title = "[-[-["+a.text+"]-]-] "
                    if proceed and a.tag == id_tag+"revision":
                        #print the_title
                        for b in a:
                            if b.tag == id_tag+"text":
                                if type (b.text) is str:
                                    text = cleanText(b.text)
                                    if '#redirect' in text:
                                        #print "redirect ignored"
                                        #print text
                                        total = total -1
                                        break ##ignore
                                    string_list.append(the_title + text + u"\n")
                                    metaCounter = metaCounter + 1
                                    counter = counter + 1
                                    ##when text tag is found and processed break out
                                    a.clear()
                                b.clear()
                                break

                elem.clear()
                if counter == files_size:
                #    update_dict(lookup_dict, string_list, metaCounter/files_size)
                    #print len(lookup_dict)
                    print "total: " + str(total)
                    print metaCounter
                    print str(skipcounter) + " skipped"
                    writeToFile(string_list, "B/part"+ str(metaCounter/files_size))
                    print "done writing"
                    counter = 0
                    skipcounter = 0
                    ##reset and go on
                    string_list = []

                #if  justsaved == False and metaCounter > 0 and metaCounter % (files_size*200) == 0:
                 #   np.save('Meta/my_file'+ str(metaCounter/(files_size*200)) +'.npy', lookup_dict)
                    justsaved = True
                    ##reset lookup_dict
                  #  lookup_dict = dict()
                   # print "Done " + str(metaCounter) + 'lines written and stored in my_file'+ str(metaCounter/(files_size*200)) +'.npy'
    #print "doing last save"
    #np.save('Meta/my_file' + str((metaCounter / (files_size * 200))+1) + '.npy', lookup_dict)
    print "done"


def GetCats(path, id_tag, files_size):
    lookup_dict = {}
    counter = 0
    metaCounter = 0
    total = 0
    string_list = []

    ##"{http://www.mediawiki.org/xml/export-0.10/}"
    #with open("/home/dzyan/Dokumenter/enwiki-20170820-pages-articles-multistream.xml") as xml:
    proceed = False
    skipcounter = 0
    current_title = "A"
    with open(path) as xml:
        for event, elem in letree.iterparse(xml, events=('start', 'end')):
            if event == "end" and elem.tag == id_tag+"page":
                total = total +1
                proceed = False
                justsaved = False
                for a in elem:
                    if a.tag == id_tag+"title":
                        if a.text == 'Cat':
                            proceed =True
                        else:
                            a.clear()
                            break
                    if a.tag == id_tag + "revision" and proceed:
                        # print the_title
                        for b in a:
                            if b.tag == id_tag + "text":
                                if type(b.text) is str:
                                    text = cleanText(b.text)
                                    string_list.append(text)
                                    writeToFile(string_list, "B/partCat")
                                    return
                 #   proceed = True

                elem.clear()
    print "done"

def basic_count(path, id_tag, files_size):
    total = 0
    with open(path) as xml:
        for event, elem in letree.iterparse(xml, events=('start', 'end'), huge_tree=True):
            if event == "end" and elem.tag == id_tag + "page":
                total = total + 1
                if total % 100000 == 0:
                    print "total pages iterated so far: " + str(total)
            elem.clear()



    print "done " + str(total)

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

def cleanText(text):
    return text.replace('\n', ' ').lower()

def writeToFile(the_list, filepath):
    print "writing " + str(len(the_list)) + " to " + filepath
    with open(filepath, "w+") as file_handler:
        for item in the_list:
            file_handler.write(item.encode('utf8'))


path = "/home/dzyan/Dokumenter/enwiki-20170820-pages-articles-multistream.xml"
tag_id = "{http://www.mediawiki.org/xml/export-0.10/}"
#basic_count(path,tag_id,200)
#parseAndWrite(path, tag_id, 400)
GetCats(path, tag_id, 400)