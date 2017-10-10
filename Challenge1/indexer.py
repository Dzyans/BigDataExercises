import os
import numpy as np
def CreateDict(dict_size):
    the_dict = dict()
    file_counter = 0
    for filename in os.listdir("B"):
       file_counter = file_counter+1
       with open("B/"+filename, 'r') as searchfile:
            filename_nr = int(filename[4:])
            cock_block_set = set()
            ##set up the set of unique words
            for line in searchfile:
                words = line.split(' ')
                for word in words:
                    cock_block_set.add(word)
            ##add them to dict
            for word in cock_block_set:
                if word in the_dict:
                    if word == ' ':
                        break  ##ignore lefter over blank sapaces
                        ##increment word count
                    # print "adding "+ word + " to dict"
                    the_dict[word].append(filename_nr)
                    # fileList.append(filename_nr)
                    # the_dict[word] = fileList
                else:
                    fileList = list()  ##key does not exist, so insert list at as value
                    fileList.append(filename_nr)
                    the_dict[word] = fileList

            #print str(len(cock_block_set)) + " words in set"
       if(file_counter > 0 and file_counter%dict_size == 0): ##time to save
            print "saving dict"
            np.save('MetaB2/BDict' + str(file_counter/dict_size) + '.npy',the_dict)
            the_dict = dict()

    print "saving last dict"
    np.save('MetaB2/BDict' + str(file_counter / dict_size) + '.npy', the_dict)


CreateDict(6000)