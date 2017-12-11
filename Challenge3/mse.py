# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 14:09:30 2017

@author: s123725
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 13:10:20 2017

@author: tadah
"""
import os

# import the necessary packages
from skimage.measure import compare_ssim as ssim
import matplotlib.pyplot as plt
import numpy as np
import cv2
import shutil, stat
import sklearn.cluster
import distance
from sklearn.metrics import jaccard_similarity_score as jcd
import timeit
from random import randrange


def keyframe(num_of_frames):
    # try running on 0KAJ1U2BPIO7.mp4, 3T7FSSZD3P6T.mp4, Z4ZMSTGKXTK3.mp4
    
    feature_lists = []
    filenames = []
    hashdict = dict()
    start_time = timeit.default_timer()
    for filename in os.listdir('.\\videos'):
        #print filename
  
        vidcap = cv2.VideoCapture('.\\videos\\' + filename)
        success,image = vidcap.read()
   
        count = 0
        success = True

        frame_counter = 0
        length = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
        
        mid = length/2
        
        startframe = mid - 50
        endframe = mid + 50
 
        hash_list = []
        while success:
            success,image = vidcap.read()
            if success:
                if (frame_counter >= startframe and frame_counter <= endframe):
        
                    difmatrix = create_differences(compare_first(image, filename))
                    _hash = my_hash(difmatrix)
                    hash_list.append(_hash)
            
                    count += 1
    
            frame_counter += 1
            if(frame_counter > endframe):
                #print ("thats enough, next mov " + str(frame_counter))
                break;
            #if (count == num_of_frames and num_of_frames is not None):
                #break;
        vidcap.release()
        hashdict[filename] = hash_list    
        #fig = plt.figure("concated"+ filename)
        #plt.imshow(vis, cmap = plt.cm.gray)
        #plt.axis("off")        
        #print 'number of feature frames: ' + str(count_feature_frames)
        #mat = create_differences(vis)
        filenames.append(filename)
        
        #hashes.append(my_hash(mat))
        #print (len(images))
        #print (count)
        #feature_lists.append(get_feature_array(hash_list, 600))
    #print (len (feature_lists))
    #print (feature_lists[1])
    elapsed = timeit.default_timer() - start_time
    print ("Vids iterated and hashed in: " + str(elapsed) + " seconds")
    print("done")
    
    loopOfDoom(hashdict)
    
    #jaccard_cluster(feature_lists, filenames)
   # print (hashdict["Z4ZMSTGKXTK3.mp4"])
    #print (hashdict["0KAJ1U2BPIO7.mp4"])
    
    print ("all done in: " + str(elapsed) + " seconds")
    print("done")    
    
    #print (hashdict)
    
    #cluster(hashes, filenames)
        #show_keyframes(keyframes, filename)

def loopOfDoom(hashdict):
    start_loop = timeit.default_timer()
    cluster_lookup = dict()
    clusters = dict()
    completed_keys = []
    cluster_nr = 0
    outer_loop_counter = 0
    hit_lookup = dict()
    cluster = []
    cluster_counter = 0
    print (len(hashdict))
    for key1 in hashdict:
        outer_loop_counter += 1
        if outer_loop_counter % 100 == 0:
            print(outer_loop_counter)
        if key1 in cluster_lookup:            
            cluster_nr = cluster_lookup[key1]
            cluster = clusters[cluster_nr]
            
        else:
            cluster_nr = cluster_counter
            cluster = []
            cluster.append(key1)
            
            clusters[cluster_nr] = cluster
            cluster_lookup[key1] = cluster_nr
            cluster_counter += 1
        
        for key2 in hashdict:
            
            hit_counter = 0
            if(key1 == key2 or key2 in completed_keys):
                
                continue
            
            for th in hashdict[key1]:
                for ch in hashdict[key2]:                    
                    if th == ch:
                        
                        hit_counter += 1
            if(hit_counter > 2):
                #match found
                
                if key2 not in clusters[cluster_nr]:
                    if key2 in hit_lookup and hit_counter > hit_lookup[key2]:
                        #we is moving the key from the old cluster
                        clusters[cluster_lookup[key2]].remove(key2)
                   
                    if key2 not in hit_lookup or hit_counter > hit_lookup[key2]:
                        clusters[cluster_nr].append(key2) 
                        cluster_lookup[key2] = cluster_nr
                        hit_lookup[key2] = hit_counter
        completed_keys.append(key1)
            
            
    
    elapsed = timeit.default_timer() - start_loop
    print ("loops of doom done in: " + str(elapsed) + " seconds")
         
    writeToFile(clusters, "results_final_doom.txt")

def compare_first(image, filename):
     
         
     height, width = image.shape[:2]
     #if(filename == "Z4ZMSTGKXTK3.mp4" or filename == "0KAJ1U2BPIO7.mp4"):
    # print (filename)
     #print ("hhh "+ str(height))
     #print ("ww "+ str(width))
     if height < width:
         heightstart = int((height/2)-100)
         heightend = int(height-((height/2)-100))
         widhtstart = int((width/2)-200)
         widthend = int(width-((width/2)-200))
     if height > width:
         heightstart = int((height/2)-200)
         heightend = int(height-((height/2)-200))
         widhtstart = int((width/2)-100)
         widthend = int(width-((width/2)-100))
    # print (heightstart)
     #print (heightend)
     #print (widhtstart)
    # print (widthend)
     image = image[heightstart:heightend, widhtstart:widthend] # Crop from x, y, w, h -> 100, 200, 300, 400
     image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
     image = cv2.resize(image, (8,9))
     return image

def get_feature_array2(frames, n_features):
    #print ("frames " + str(len(frames)))
    hashed_features = np.zeros(n_features, dtype=int)
    col = 0
    for frame in frames:
        dif_matrix = create_differences(frame)
        #print (dif_matrix)
        _hash = my_hash(dif_matrix)
        index = int_generator(_hash) % n_features
        if hashed_features[index] >= 1:
            col = col +1
            #print ("coll on index " + str(index))
        hashed_features[index] = 1
    #print (col)    
    return hashed_features

def get_feature_array(hashes, n_features):
    #print ("frames " + str(len(frames)))
    hashed_features = np.zeros(n_features, dtype=int)
    col = 0
    for _hash in hashes:
        
        index = int_generator(_hash) % n_features
        if hashed_features[index] >= 1:
            col = col +1
            #print ("coll on index " + str(index))
        hashed_features[index] = 1
    #print (col)    
    for i in range (0, len(hashed_features)):
        if hashed_features[i] != 1:
            hashed_features[i] = randrange(4, 102311, 2)
    return hashed_features

def int_generator(LSH_hashed_string):
    #print (LSH_hashed_string)
    value = 0
    counter = 0
    for char in LSH_hashed_string:
        value += ord(char) + counter*4242
        if counter % 7 == 0:
            counter = 0
        counter += 1
    return value

def show_keyframes(keyframes,filename):
    #print (len(keyframes))
    # loop over the images
    fig = plt.figure("Images"+ filename)
    for (i, (image)) in enumerate(keyframes):
    	# show the image
    	ax = fig.add_subplot(6, 10, i + 1)
    	plt.imshow(image, cmap = plt.cm.gray)
    	plt.axis("off")
     
    # show the figure
    #plt.show()
def pre_compare(keyframe,image):
    #crop the image
    height, width = image.shape[:2]
    keyframe = keyframe[20:height-20, 20:width-20] # Crop from x, y, w, h -> 100, 200, 300, 400
    image = image[20:height-20, 20:width-20] # Crop from x, y, w, h -> 100, 200, 300, 400

    #greyscale the image
    keyframe = cv2.cvtColor(keyframe, cv2.COLOR_BGR2GRAY)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # pixelize the image
    keyframe = cv2.resize(keyframe, (8,9))
    image = cv2.resize(image, (8,9))
    # compare the images
    simm, error = compare_images(keyframe, image)
    return simm, error ,keyframe

def writeToFile(hashdict, filepath):
    #print "writing " + str(len(the_list)) + " to " + filepath
    start_time = timeit.default_timer()
    with open(filepath, "a") as file_handler:
        for key in hashdict:
            for val in hashdict[key]:                
                file_handler.write(val.replace(' ', '')[:-4].upper() + " ")
            file_handler.write("\n")
    elapsed = timeit.default_timer() - start_time
    print ("wrting to file done in: " + str(elapsed))

def mse(imageA, imageB):
	# the 'Mean Squared Error' between the two images is the
	# sum of the squared difference between the two images;
	# NOTE: the two images must have the same dimension
	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	err /= float(imageA.shape[0] * imageA.shape[1])
	
	# return the MSE, the lower the error, the more "similar"
	# the two images are
	return err
 
def compare_images(imageA, imageB):
    # compute the mean squared error and structural similarity
    # index for the images
    m = mse(imageA, imageB)
    s = ssim(imageA, imageB)

    return m,s
    
#input source of the videos
def create_subset(source):
    #files = ['0KAJ1U2BPIO7.mp4']
    files = ['0B0A9DAX03KT.mp4','0CFF1YUSITJE.mp4','0KAJ1U2BPIO7.mp4', '3T7FSSZD3P6T.mp4', 'Z4ZMSTGKXTK3.mp4','00SXM76KD1X2.mp4']
    dest = '.\subsubvideos'
    for the_file in os.listdir(dest):
        file_path = os.path.join(dest, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path): shutil.rmtree(file_path)
        except Exception as e:
            print(e)
    for file in files:
        file_path = os.path.join(source, file)
        os.chmod(dest, stat.S_IWRITE)
        shutil.copy(file_path, dest)

# Function to create hash (from David on Aula)
def my_hash(differences):
    
    hexi = ''
    for difference in differences:
        decimal_value = 0
        hex_string = []
        for index, value in enumerate(difference):
            #print ("index "+ str(index))
            if value:
                decimal_value += 2**(index % 3)
            if (index % 3) == 2:
                hex_string.append(hex(decimal_value)[2:].rjust(2, '0'))
                decimal_value = 0
            if (index % 4) == 1:
                hex_string.append(hex(decimal_value)[2:].rjust(2, '0'))
            if not value:
               decimal_value += 4**(index % 5)
        hexi += (''.join(''.join(hex_string)))
    #print ("-------------------------------------------------------")
    #print (hexi)
    return hexi

# Function to create difference matrix
def create_differences(img_matrix):
    sz_row = img_matrix.shape[0]
    sz_col = img_matrix.shape[1] - 1
    # Create empty np matrix with booleans
    mat = np.zeros((sz_row,sz_col), dtype=bool)
    for row in range(img_matrix.shape[0]):
        for col in range(img_matrix.shape[1] - 1):
            
            if img_matrix[row,col] > img_matrix[row, col+1]:
                mat[row,col] = True
            else:
                mat[row,col] = False

    return mat

def jaccard_cluster(mov_features, mov_names):
    #print (len(words))
    #print (mov_features)
    clusters = dict()
    #mov_features = np.asarray(mov_features) #So that indexing with a list will work
    print ("calculating sim matrix")
    start_time = timeit.default_timer()
    for hej in mov_features:
        for kek in mov_features:
            print(np.intersect1d(hej,kek))
    lev_similarity = np.array([[jcd(np.asanyarray(w1),np.asanyarray(w2)) for w1 in mov_features] for w2 in mov_features])
    elapsed = timeit.default_timer() - start_time
    print ("sim calculated in: " + str(elapsed) + " seconds")
    print("done")
    #print (len(lev_similarity))
    #print (lev_similarity2)
    affprop = sklearn.cluster.AffinityPropagation()
    affprop.fit(lev_similarity)
    #print (affprop.labels_)
    
    #for i in range(0, len(affprop.labels_)):
        #print(str(affprop.labels_[i]) + " " + mov_names[i])
        #print (filenames[i])
    print ("gathering results")
    for i in range (0, len(affprop.labels_)):
        print (affprop.labels_[i])
        print (mov_names[i])
        
        if affprop.labels_[i] not in clusters:
            vids = []
            vids.append(mov_names[i])
            clusters[affprop.labels_[i]] = vids
        else:
            clusters[affprop.labels_[i]].append(mov_names[i])
    writeToFile(clusters, "jaccard_results_all.txt")
    print("done")  
    print(clusters)
    
#create_subset('videos')
keyframe(None)