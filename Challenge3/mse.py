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
from shutil import copyfile
import os, shutil, stat


def keyframe(num_of_frames):
    # try running on 0KAJ1U2BPIO7.mp4, 3T7FSSZD3P6T.mp4, Z4ZMSTGKXTK3.mp4
    for filename in os.listdir('.\subsubvideos'):
        #print filename
        vidcap = cv2.VideoCapture('.\\subsubvideos\\' + filename)
        success,image = vidcap.read()
        keyframes = []
        count = 0
        success = True
        while success:
            success,image = vidcap.read()
            if success:
                height, width = image.shape[:2]
                #print( image.shape)
                #print ( height)
                #print ( width)
                
                if (count == 0):
                    keyframe = image
                    keyframes.append(keyframe[20:height-20, 20:width-20])
                else:
                    error, simm, _keyframe = pre_compare(keyframe,image)
                    
                    if (simm < 0.60):
                        keyframe = image
                        keyframes.append(_keyframe)
                count += 1
            if (count == num_of_frames and num_of_frames is not None):
                break;
        vidcap.release()
        #print 'number of feature frames: ' + str(count_feature_frames)
        show_keyframes(keyframes, filename)

def show_keyframes(keyframes,filename):
    print (len(keyframes))
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

create_subset('videos')
keyframe(None)