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

def keyframe(num_of_frames):
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
                if (count == 0):
                    keyframe = image
                    keyframes.append(keyframe)
                else:
                    error, simm = pre_compare(keyframe,image)
                    
                    if (simm < 0.60):
                        print error, simm
                        keyframe = image
                        keyframes.append(keyframe)
                count += 1
            if (count == num_of_frames and num_of_frames is not None):
                break;
        vidcap.release()
        #print 'number of feature frames: ' + str(count_feature_frames)
        show_keyframes(keyframes)

def show_keyframes(keyframes):
    print len(keyframes)
    # loop over the images
    fig = plt.figure("Images")
    for (i, (image)) in enumerate(keyframes):
    	# show the image
    	ax = fig.add_subplot(6, 6, i + 1)
    	plt.imshow(image, cmap = plt.cm.gray)
    	plt.axis("off")
     
    # show the figure
    #plt.show()
def pre_compare(keyframe,image):
    #greyscale the image
    keyframe = cv2.cvtColor(keyframe, cv2.COLOR_BGR2GRAY)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # pixelize the image
    keyframe = cv2.resize(keyframe, (8,9))
    image = cv2.resize(image, (8,9))

    # initialize the figure
    #fig = plt.figure("Images")
    #images = ("keyframe", keyframe), ("image", image)
     
    # loop over the images
    #for (i, (name, image)) in enumerate(images):
    	# show the image
    	#ax = fig.add_subplot(1, 3, i + 1)
    	#ax.set_title(name)
    	#plt.imshow(image, cmap = plt.cm.gray)
    	#plt.axis("off")
     
    # show the figure
    #plt.show()
 
    # compare the images
    return compare_images(keyframe, image, "Original vs. Contrast")

def mse(imageA, imageB):
	# the 'Mean Squared Error' between the two images is the
	# sum of the squared difference between the two images;
	# NOTE: the two images must have the same dimension
	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	err /= float(imageA.shape[0] * imageA.shape[1])
	
	# return the MSE, the lower the error, the more "similar"
	# the two images are
	return err
 
def compare_images(imageA, imageB, title):
    # compute the mean squared error and structural similarity
    # index for the images
    m = mse(imageA, imageB)
    s = ssim(imageA, imageB)
    
    # setup the figure
    #fig = plt.figure(title)
    #plt.suptitle("MSE: %.2f, SSIM: %.2f" % (m, s))
    
    # show first image
    #ax = fig.add_subplot(1, 2, 1)
    #plt.imshow(imageA, cmap = plt.cm.gray)
    #plt.axis("off")
 
    # show the second image
    #ax = fig.add_subplot(1, 2, 2)
    #plt.imshow(imageB, cmap = plt.cm.gray)
    #plt.axis("off")
    
    # show the images
    #plt.show()
    return m,s


keyframe(None)