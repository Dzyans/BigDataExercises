import numpy as np
import xml.etree.ElementTree as etree
def parseAndWrite(path, id_tag, files_size):
    lookup_dict = {}
    counter = 0
    metaCounter = 0
    string_list = []
    ##"{http://www.mediawiki.org/xml/export-0.10/}"
    #with open("/home/dzyan/Dokumenter/enwiki-20170820-pages-articles-multistream.xml") as xml:
    current_title = "A"
    with open(path) as xml:
        for event, elem in etree.iterparse(xml, events=('start', 'end')):
            if event == "end" and elem.tag == id_tag+"page":
                for a in elem:
                    if a.tag == id_tag+"title":
                        if a.text == 'A' or a.text[0] == 'a':
                            break
                        the_title = "[-[-["+a.text+"]-]-]"
                    if a.tag == id_tag+"revision":
                        for b in a:
                            if b.tag == id_tag+"text":
                                if type (b.text) is str:
                                    text = cleanText(b.text)
                                    if '#redirect' in text:
                                        #print "redirect ignored"
                                        #print text
                                        break ##ignore
                                    string_list.append(the_title + text + u"\n")
                                    metaCounter = metaCounter + 1
                                    counter = counter + 1
                                    ##when text tag is found and processed break out
                                break


                if counter == files_size:
                    #update_dict(lookup_dict, string_list, metaCounter/files_size)
                    print len(lookup_dict)
                    writeToFile(string_list, "B/part"+ str(metaCounter/files_size))
                    counter = 0
                    ##reset and go on
                    string_list = []
                elem.clear()
                if metaCounter > 0 and metaCounter % (files_size*1000) == 0:
                    #np.save('Meta/my_file'+ str(metaCounter/(files_size*1000)) +'.npy', lookup_dict)
                    ##reset lookup_dict
                    #lookup_dict = dict()
                    print "Done " + str(metaCounter) + 'lines written and stored in my_file'+ str(metaCounter/(files_size*1000)) +'.npy'





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
parseAndWrite(path, tag_id, 200)