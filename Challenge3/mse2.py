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
import timeit

def keyframe(num_of_frames):
  
    # try running on 0KAJ1U2BPIO7.mp4, 3T7FSSZD3P6T.mp4, Z4ZMSTGKXTK3.mp4
    counter = 0
    hashes = []
    filenames = []
    for filename in os.listdir('.\subsubvideos'):
        #print filename
        
        vidcap = cv2.VideoCapture('.\\subsubvideos\\' + filename)
                
        success,image = vidcap.read()
        keyframes = []
        count = 0
        success = True
        vis = None
        while success:
            success,image = vidcap.read()
            if success:
                height, width = image.shape[:2]
                #print( image.shape)
                #print ( height)
                #print ( width)
                
                if (count == 0):
                    keyframe = image
                    vis = compare_first(keyframe)
                else:
                    error, simm, _keyframe = pre_compare(keyframe,image)
                    if (simm < 0.60):
                        keyframe = image
                        keyframes.append(_keyframe)
                        vis = np.concatenate((vis,_keyframe),axis=1)
                count += 1
            if (count == num_of_frames and num_of_frames is not None):
                break;
        vidcap.release()
        filenames.append(filename);
        #fig = plt.figure("concated"+ filename)
        #plt.imshow(vis, cmap = plt.cm.gray)
        #plt.axis("off")        
        #print 'number of feature frames: ' + str(count_feature_frames)
        mat = create_differences(vis)
        counter = counter +1
        hashes.append(my_hash(mat))
        #print("neeext " + str(counter))
        #print (len(hashes))
    cluster(hashes, filenames)
        #show_keyframes(keyframes, filename)
def compare_first(image):     
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
     
     image = image[heightstart:heightend, widhtstart:widthend] # Crop from x, y, w, h -> 100, 200, 300, 400
     image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
     image = cv2.resize(image, (8,9))
     return image


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
   
    keyframe = keyframe[heightstart:heightend, widhtstart:widthend]
    image = image[heightstart:heightend, widhtstart:widthend] # Crop from x, y, w, h -> 100, 200, 300, 400

    #greyscale the image
    keyframe = cv2.cvtColor(keyframe, cv2.COLOR_BGR2GRAY)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # pixelize the image
    keyframe = cv2.resize(keyframe, (8,9))
    image = cv2.resize(image, (8,9))
    # compare the images
    simm, error = compare_images(keyframe, image)
    return simm, error ,keyframe

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
    files = ['0KAJ1U2BPIO7.mp4', '3T7FSSZD3P6T.mp4', 'Z4ZMSTGKXTK3.mp4']
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
            if value:
                decimal_value += 2**(index % 8)
            if (index % 8) == 7:
                hex_string.append(hex(decimal_value)[2:].rjust(2, '0'))
                decimal_value = 0
        hexi += (''.join(''.join(hex_string)))
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

def cluster(words, filenames):
    clusters = dict()
    words = np.asarray(words) #So that indexing with a list will work
    print ("calculating similarity on " + str(len(words)) + " items")
    
    start_time = timeit.default_timer()
    lev_similarity = -1*np.array([[distance.levenshtein(w1,w2) for w1 in words] for w2 in words])
    elapsed = timeit.default_timer() - start_time
    print ("sim calculated in: " + str(elapsed) + " seconds")
    print("done")
    
    affprop = sklearn.cluster.AffinityPropagation(affinity="precomputed", damping=0.5)

    print("fitting and clustering")
    affprop.fit(lev_similarity)
    print("done")
    
    print ("gathering results")
    for i in range (0, len(affprop.labels_)):
        
        
        if affprop.labels_[i] not in clusters:
            vids = []
            vids.append(filenames[i])
            clusters[affprop.labels_[i]] = vids
        else:
            clusters[affprop.labels_[i]].append(filenames[i])
    writeToFile(clusters, "levenshtein_results_all.txt")
    print("done")  
    print(clusters)
        
    #for cluster_id in np.unique(affprop.labels_):
     #   exemplar = videos[affprop.cluster_centers_indices_[cluster_id]]
      #  cluster = np.unique(videos[np.nonzero(affprop.labels_==cluster_id)])
       # cluster_str = ", ".join(cluster)
        #print(" - *%s:* %s" % (exemplar, cluster_str))
    return clusters
#create_subset('videos')
keyframe(None)